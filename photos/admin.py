from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_featured')
    search_fields = ('title', 'description')

# Register the Photo model with the PhotoAdmin
admin.site.register(Photo, PhotoAdmin)