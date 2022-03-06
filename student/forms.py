from django.forms import ModelForm
from .models import Room

class Roomform(ModelForm):

    class Meta:
        model=Room
        exclude = ('created_by',)