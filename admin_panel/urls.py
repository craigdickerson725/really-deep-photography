from django.urls import path
from .views import (
    AdminPanelView, EditPhotoView, DeletePhotoView,
    FAQCRUDView, FAQDeleteView, NoPermissionView
)

urlpatterns = [
    # Admin panel main page
    path('', AdminPanelView.as_view(), name='admin_panel'),

    # Photo management
    path('edit_photo/<int:photo_id>/', EditPhotoView.as_view(), name='edit_photo'),
    path('delete_photo/<int:photo_id>/', DeletePhotoView.as_view(), name='delete_photo'),

    # FAQ management
    path('faq_crud/', FAQCRUDView.as_view(), name='faq_crud'),
    path('faq_delete/', FAQDeleteView.as_view(), name='faq_delete'),

    # No permission page
    path('no_permission/', NoPermissionView.as_view(), name='no_permission'),
]
