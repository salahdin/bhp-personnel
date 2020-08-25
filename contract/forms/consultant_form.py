from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Consultant


class ConsultantForm(SiteModelFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsultantForm, self).__init__(*args, **kwargs)
        self.fields['pid'].required = False

    pid = forms.CharField(
        label='Consultant/PI Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Consultant
        fields = '__all__'
