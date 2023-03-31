from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    # нужно дописать ссылку для входа на сайт
]
