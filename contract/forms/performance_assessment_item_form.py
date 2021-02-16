from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import PerformanceAssessmentItem


class PerformanceAssessmentItemForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = PerformanceAssessmentItem
        fields = '__all__'
