from django.urls import path
from .views import (
    index, AboutView, ContactView,
)

urlpatterns = [
    # Home page
    path('', index, name='home'),

    # Static pages
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
