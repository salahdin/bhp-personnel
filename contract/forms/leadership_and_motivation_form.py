from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import LeadershipAndMotivation


class LeadershipAndMotivationForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = LeadershipAndMotivation
        fields = '__all__'
