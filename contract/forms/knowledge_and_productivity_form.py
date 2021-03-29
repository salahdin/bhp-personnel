from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import KnowledgeAndProductivity


class KnowledgeAndProductivityForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = KnowledgeAndProductivity
        fields = '__all__'
