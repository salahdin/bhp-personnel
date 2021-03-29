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

        performance_assessment_item = self.data.get(
            'performanceassessmentitem_set-TOTAL_FORMS')

        overall_perf_score = 0
        for i in range(int(performance_assessment_item)):
            kpa_rating = self.data.get(
                'performanceassessmentitem_set-' + str(i) +'-kpa_rating'
            )
            import pdb; pdb.set_trace()
            overall_perf_score = overall_perf_score + int(kpa_rating)

    class Meta:
        model = PerformanceAssessment
        fields = '__all__'
