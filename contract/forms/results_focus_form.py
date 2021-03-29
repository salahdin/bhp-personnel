from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import ResultsFocus


class ResultsFocusForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ResultsFocus
        fields = '__all__'
