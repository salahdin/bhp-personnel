from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import ProfessionalSkills


class ProfessionalSkillsForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ProfessionalSkills
        fields = '__all__'
