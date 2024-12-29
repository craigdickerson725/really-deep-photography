from django import forms
from .models import FAQ


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'question': 'FAQ Question',
            'answer': 'FAQ Answer',
        }
