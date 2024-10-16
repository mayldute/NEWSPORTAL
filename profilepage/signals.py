from django.contrib.auth.models import Group
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django.db.models.signals import m2m_changed
from django.core.mail import send_mail
from posts.models import PostCategory, UserCategorySubscription
from django.conf import settings
from urllib.parse import urljoin


@receiver(user_signed_up)
def add_user_to_group(request, user, **kwargs):
    group = Group.objects.get(name='common') 
    user.groups.add(group)
    
    
@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscriptions = UserCategorySubscription.objects.filter(category__in=categories)
        unique_users_email = set(subscription.user.email for subscription in subscriptions)
        
        for user_email in unique_users_email:
            post_url = urljoin(settings.BASE_URL, reverse('post_detail', kwargs={'pk': instance.pk}))
            
            html_message = render_to_string('profile/notify_about_new_post.html', {
                'title': instance.title,
                'preview': instance.preview(),
                'post_url': post_url  
            })
            
            send_mail(
                subject=f'Вышла новая статья!',
                message='',
                html_message=html_message,
                recipient_list=[user_email],
                from_email=settings.DEFAULT_FROM_EMAIL,
                fail_silently=False,
                )
        
