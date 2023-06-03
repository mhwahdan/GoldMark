from django.urls import path
from .views import view_faqs

urlpatterns = [
   path('', view_faqs, name='faqs')
]
