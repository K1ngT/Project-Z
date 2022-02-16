from django.forms import ModelForm
from .models import Asset, Locations

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

class LocationsForm(ModelForm):
    class Meta:
        model = Locations
        fields= '__all__'