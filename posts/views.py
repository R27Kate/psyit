from django.shortcuts import get_object_or_404, render, redirect

from django.core.paginator import Paginator

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import Post, User, Article


#@login_required
def index(request):
    # получаем список последних постов пользователей
    latest_posts = Post.objects.all().order_by('-created_at')[:5]

    # получаем список новых статей
    new_articles = Article.objects.all().order_by('-created_at')[:3]

# получаем картинку на сегодняшний день
    today_image = get_today_image()

    # передаем данные в шаблон
    return render(request, 'index.html', {'today_image': today_image,
                                           'latest_posts': latest_posts,
                                           'new_articles': new_articles})

# функция для получения картинки на сегодняшний день
def get_today_image():
    # здесь должен быть код для получения картинки на сегодняшний день
    # например, можно использовать API, который каждый день возвращает новую картинку
    return 'https://via.placeholder.com/500x200.png?text=Today%27s+Image'