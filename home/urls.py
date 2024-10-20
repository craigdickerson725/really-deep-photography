from django.contrib import admin
from django.urls import path
from .views import index, GalleryView, AboutView, ContactView
from allauth.account.views import LoginView

urlpatterns = [
    path('', index, name='home'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='account_login'),  # Use Allauth's login view
]