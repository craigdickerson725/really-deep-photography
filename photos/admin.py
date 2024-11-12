from django.contrib import admin
from .models import Photo
from .forms import PhotoForm

class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm  # Use the custom form with validation
    list_display = ('id', 'title', 'price', 'is_featured')
    search_fields = ('title', 'description')

# Register the Photo model with the PhotoAdmin
admin.site.register(Photo, PhotoAdmin)