from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import PlanningSkills


class PlanningSkillsForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = PlanningSkills
        fields = '__all__'
