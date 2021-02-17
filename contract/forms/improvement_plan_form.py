from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import ImprovementPlan


class ImprovementPlanForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ImprovementPlan
        fields = '__all__'
