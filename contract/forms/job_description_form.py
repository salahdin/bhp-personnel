from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import JobDescription


class JobDescriptionForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = '__all__'
