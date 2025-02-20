from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('why/', views.why, name='why'),
    path('price-inquiry/', views.price_inquiry, name='price'),
]
