from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import KeyPerformanceArea


class KeyPerformanceAreaForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = KeyPerformanceArea
        fields = '__all__'


