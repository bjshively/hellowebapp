from django.forms import ModelForm
from collection.models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'description',)