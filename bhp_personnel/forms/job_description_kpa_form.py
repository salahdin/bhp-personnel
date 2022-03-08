from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import JobDescriptionKpa


class JobDescriptionKpaForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = JobDescriptionKpa
        fields = '__all__'
