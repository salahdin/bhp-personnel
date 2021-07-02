from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import PerformanceAssessment


class PerformanceAssessmentForm(SiteModelFormMixin, forms.ModelForm):

    emp_identifier = forms.CharField(
        label='Employee Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    overall_perf_score = forms.CharField(
        label='Overall Performance Score',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        super().clean()

    class Meta:
        model = PerformanceAssessment
        fields = '__all__'
