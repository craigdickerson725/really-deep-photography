from django.urls import path
from . import views
from .views import index

urlpatterns = [
    # Home page
    path('', views.index, name='home'),
]
