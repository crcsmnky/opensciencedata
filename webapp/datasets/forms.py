from django.forms import ModelForm
from datasets.models import Dataset

class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = ('name', 'description', 'data')


