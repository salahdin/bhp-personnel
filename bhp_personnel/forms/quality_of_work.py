from django import forms

from edc_base.sites import SiteModelFormMixin
from ..choices import ASSESSMENT_TYPE
from ..models import QualityOfWork


class QualityOfWorkForm(SiteModelFormMixin, forms.ModelForm):

    assessment_period_type = forms.ChoiceField(
        label='Period of ASSESSMENT',
        widget=forms.RadioSelect(),
        choices=ASSESSMENT_TYPE)

    class Meta:
        model = QualityOfWork
        fields = '__all__'
