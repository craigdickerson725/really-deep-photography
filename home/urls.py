from django.urls import path
from .views import index, GalleryView, AboutView, ContactView, search, photo_detail

urlpatterns = [
    # Home page
    path('', index, name='home'),
    # Gallery page
    path('gallery/', GalleryView.as_view(), name='gallery'),
    # About page
    path('about/', AboutView.as_view(), name='about'),
    # Contact page
    path('contact/', ContactView.as_view(), name='contact'),
    # Search functionality
    path('search/', search, name='search'),
    # Photo details page
    path('photo/<int:photo_id>/', photo_detail, name='photo_detail'),
]
