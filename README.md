# NEWSPORTAL

# >>> from news.models import *

# >>> user1 = User.objects.create_user('user1')
# >>> user2 = User.objects.create_user('user2')

# >>> author1 = Author.objects.create(user=user1)
# >>> author2 = Author.objects.create(user=user2)

# >>> Category.objects.create(name='Category1')
# >>> Category.objects.create(name='Category2')
# >>> Category.objects.create(name='Category3')
# >>> Category.objects.create(name='Category4')

# >>> post1 = Post.objects.create(type='AR', title='Post 1', text='Text of Post 1', author=author1)
# >>> post2 = Post.objects.create(type='AR', title='Post 2', text='Text of Post 2', author=author2)
# >>> news1 = Post.objects.create(type='NW', title='News 1', text='Text of News 1', author=author1)

# >>> category1 = Category.objects.get(name='Category1')
# >>> category2 = Category.objects.get(name='Category2')
# >>> category3 = Category.objects.get(name='Category3')
# >>> category4 = Category.objects.get(name='Category4')
# >>> post1.category.add(category1, category2, category4)
# >>> post2.category.add(category3, category4)
# >>> news1.category.add(category1, category2, category3)

# >>> comment1 = Comment.objects.create(post=post1, text='Comment 1', user=user1)
# >>> comment2 = Comment.objects.create(post=post2, text='Comment 2', user=user1)
# >>> comment3 = Comment.objects.create(post=post1, text='Comment 3', user=user2)
# >>> comment4 = Comment.objects.create(post=news1, text='Comment 4', user=user2)

# >>> post1.like()
# >>> post2.like()
# >>> post1.like()
# >>> news1.like()
# >>> comment1.like()
# >>> comment3.like()
# >>> comment2.like()
# >>> comment3.like()
# >>> comment3.dislike()
# >>> comment4.like()
# >>> comment3.like()

# >>> user1 = User.objects.get(username='user1')
# >>> user2 = User.objects.get(username='user2')
# >>> author1 = Author.objects.get(user=user1)
# >>> author2 = Author.objects.get(user=user2)
# >>> author1.update_rating()
# >>> author2.update_rating()

# >>> best_user = Author.objects.order_by('-rating').first()
# >>> print(f'Username лучшего пользователя: {best_user.user.username}, рейтинг: {best_user.rating}')

# >>> best_post = Post.objects.filter(type='AR').order_by('-rating').first()
# >>> print(f'Дата добавления: {best_post.create_time}, Username автора: {best_post.author.user.username}, Рейтинг: {best_post.rating}, Заголовок: {best_post.title}, Превью: {best_post.preview()}') 
# >>> comments_to_best_post = Comment.objects.filter(post=best_post)
# >>> print('\n'.join([f'Дата: {comment.create_time}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.text}' for comment in comments_to_best_post])) 