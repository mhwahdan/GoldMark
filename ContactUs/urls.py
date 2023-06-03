from django.urls import path
from . import views

urlpatterns = [
    path('message', views.submitContactForm, name='sendMessage'),
    path('', views.contact_us, name='ContactUs')
]