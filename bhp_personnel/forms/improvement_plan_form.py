from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import ImprovementPlan, ImprovementObjectives


class ImprovementPlanForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ImprovementPlan
        fields = '__all__'


class ImprovementObjectivesForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ImprovementObjectives
        fields = '__all__'
