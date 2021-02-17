from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import ImprovementObjectives


class ImprovementObjectivesForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ImprovementObjectives
        fields = '__all__'
