from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import PerformanceAssessment


class PerformanceAssessmentForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = PerformanceAssessment
        fields = '__all__'
