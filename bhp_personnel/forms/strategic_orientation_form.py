from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import StrategicOrientation


class StrategicOrientationForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = StrategicOrientation
        fields = '__all__'
