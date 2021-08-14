from django.forms import ModelForm
from .models import Unit



class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
