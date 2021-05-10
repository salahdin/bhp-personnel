from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import ImprovementObjectives, PerformanceImpPlan


class PerformanceImpPlanForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = PerformanceImpPlan
        fields = '__all__'


class ImprovementObjectivesForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ImprovementObjectives
        fields = '__all__'
