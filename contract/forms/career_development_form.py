from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import CareerDevelopment


class CareerDevelopmentForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = CareerDevelopment
        fields = '__all__'
