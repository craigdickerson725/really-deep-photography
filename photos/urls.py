from django.urls import path
from .views import (
    GalleryView, photo_detail, search
)

urlpatterns = [
    # Gallery and photo details
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('photo/<int:photo_id>/', photo_detail, name='photo_detail'),

    # Search functionality
    path('search/', search, name='search'),
]
