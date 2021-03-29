from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import InnovationAndCreativity


class InnovationAndCreativityForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = InnovationAndCreativity
        fields = '__all__'
