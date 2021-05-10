from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import CommunicationSkills


class CommunicationSkillsForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = CommunicationSkills
        fields = '__all__'
