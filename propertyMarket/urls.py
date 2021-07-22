from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property', views.view_property, name='properties'),
    path('message', views.process_message, name='sendMessage'),
    path('searchproperties', views.search_properties, name='search_property')
]