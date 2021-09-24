from django.urls import path
from Blog import views

urlpatterns = [
    path('blogs', views.blogs, name='Blogs'),
    path('showblog', views.show_blog, name='ShowBlog')
]
