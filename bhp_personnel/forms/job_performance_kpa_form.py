from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import JobPerformanceKpa

class JobPerformanceKpaForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = JobPerformanceKpa
        fields = '__all__'
