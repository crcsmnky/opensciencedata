from django import forms
from datasets.models import Dataset

class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        # fields = ('name', 'description', 'data')
        exclude = ('uploaded', 'updated', 'user', 'downloads')
        widgets = {
            'name': forms.TextInput(attrs={'class':'span8'}),
            'description': forms.Textarea(attrs={'class':'span8', 'rows':10}),
            'tags': forms.TextInput(attrs={'class':'span8'}),
        }

