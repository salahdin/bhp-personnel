from django import forms

from edc_base.sites import SiteModelFormMixin
from ..choices import ASSESSMENT_TYPE
from ..models import ProfessionalSkills


class ProfessionalSkillsForm(SiteModelFormMixin, forms.ModelForm):

    assessment_period_type = forms.ChoiceField(
        label='Period of ASSESSMENT',
        widget=forms.RadioSelect(),
        choices=ASSESSMENT_TYPE)

    class Meta:
        model = ProfessionalSkills
        fields = '__all__'
