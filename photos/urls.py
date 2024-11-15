from django.urls import path
from .views import (
    GalleryView, photo_detail, AdminPanelView, EditPhotoView,
    DeletePhotoView, search, NoPermissionView
)

urlpatterns = [
    # Gallery and photo details
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('photo/<int:photo_id>/', photo_detail, name='photo_detail'),

    # Search functionality
    path('search/', search, name='search'),

    # Admin panel for site owner
    path('admin_panel/', AdminPanelView.as_view(), name='admin_panel'),
    path('admin_panel/edit/<int:photo_id>/', EditPhotoView.as_view(), name='edit_photo'),  # noqa
    path('admin_panel/delete/<int:photo_id>/', DeletePhotoView.as_view(), name='delete_photo'),  # noqa

    # No permission page
    path('no_permission/', NoPermissionView.as_view(), name='no_permission'),
]
