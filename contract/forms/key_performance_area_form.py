from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import KeyPerformanceArea, KeyPerformanceAreaItem


class KeyPerformanceAreaForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = KeyPerformanceArea
        fields = '__all__'


class KeyPerformanceAreaItemForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = KeyPerformanceAreaItem
        fields = '__all__'
