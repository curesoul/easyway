from django.conf import settings
from django.contrib import admin
from django.urls import path

from .views import homepage, post, category_post_list, allposts


app_name = 'posts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('post/<slug>/', post, name='post'),
    path('postlist/<slug>/', category_post_list, name='postlist'),
    path('posts/', allposts, name='allposts'),
]