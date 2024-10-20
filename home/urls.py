from django.urls import path
from .views import index, GalleryView, AboutView, ContactView, search

urlpatterns = [
    path('', index, name='home'),  # Home page
    path('gallery/', GalleryView.as_view(), name='gallery'),  # Gallery page
    path('about/', AboutView.as_view(), name='about'),  # About page
    path('contact/', ContactView.as_view(), name='contact'),  # Contact page
    path('search/', search, name='search'),  # Search functionality
]
