from django import forms
from django.core.exceptions import ValidationError
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'size', 'price', 'is_featured']  # noqa

    def clean_is_featured(self):
        is_featured = self.cleaned_data.get('is_featured')
        if is_featured:
            # Count currently featured photos,
            # excluding the current instance if it already exists
            featured_count = Photo.objects.filter(is_featured=True).exclude(pk=self.instance.pk).count()  # noqa
            if featured_count >= 3:
                raise ValidationError("There can only be up to 3 featured photos at a time.")  # noqa
        return is_featured
