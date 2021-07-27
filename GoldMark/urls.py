from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property', views.view_property, name='properties'),
    path('message', views.process_message, name='sendMessage'),
    path('searchproperties', views.search_properties, name='search_property'),
    path('FAQS', views.view_faqs, name='FAQS'),
    path('contact', views.contact_us, name='ContactUs'),
    path('blogs', views.blogs, name='Blogs'),
    path('showblog', views.show_blog, name='ShowBlog')
]
