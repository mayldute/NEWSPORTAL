import logging
 
from django.conf import settings
 
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.utils import timezone
from datetime import timedelta
from posts.models import Post, PostCategory, Category, UserCategorySubscription
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from collections import defaultdict
 
logger = logging.getLogger(__name__)
 
 
def weelky_notify():
    one_week_ago = timezone.now() - timedelta(days=7)
    recent_posts = Post.objects.filter(create_time__gte=one_week_ago)
    categories = Category.objects.filter(id__in=PostCategory.objects.filter(post__in=recent_posts).values('category_id')).distinct()
    subscriptions = UserCategorySubscription.objects.filter(category__in=categories)
    unique_user_email = set(subscription.user.email for subscription in subscriptions) 
    
    for user_email in unique_user_email:
        user_posts = [] 
        for subscription in subscriptions:
            category_id = subscription.category.id
            posts_for_category = recent_posts.filter(postcategory__category_id=category_id)
            user_posts.extend(posts_for_category)

        user_posts = sorted(set(user_posts), key=lambda post: post.create_time, reverse=True)
        
        html_message = render_to_string('profile/weekly_notify_posts.html', {
            'user_posts': user_posts,
            })
                
        send_mail(
            subject=f'Статьи за последнюю неделю!',
            message='',
            html_message=html_message,
            recipient_list=[user_email],
            from_email=settings.DEFAULT_FROM_EMAIL,
            fail_silently=False,
        )
        
            
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)
 
 
class Command(BaseCommand):
    help = "Runs apscheduler."
 
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        
        scheduler.add_job(
            weelky_notify,
            trigger=CronTrigger(day_of_week='wed', hour=12, minute=0), 
            id="weelky_notify", 
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'weelky_notify'.")
 
        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ), 
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )
 
        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
 