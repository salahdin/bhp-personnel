from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Consultant


class ConsultantForm(SiteModelFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsultantForm, self).__init__(*args, **kwargs)
        self.fields['identifier'].required = False

    identifier = forms.CharField(
        label='Consultant Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Consultant
        fields = '__all__'
