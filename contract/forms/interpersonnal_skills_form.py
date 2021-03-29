from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import InterpersonalSkills


class InterpersonalSkillsForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = InterpersonalSkills
        fields = '__all__'
