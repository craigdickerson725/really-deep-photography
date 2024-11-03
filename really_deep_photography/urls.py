from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # This includes allauth's login/logout URLs
    path('', include('home.urls')),
    path('photos/', include('photos.urls')),
    path('cart/', include('cart.urls')),
]
