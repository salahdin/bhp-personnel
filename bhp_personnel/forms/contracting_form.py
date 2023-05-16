from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Contracting, Contract


class ContractingForm(SiteModelFormMixin, forms.ModelForm):
    contract = forms.ModelChoiceField(label='Contract', queryset=Contract.objects.all(),
                                      widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['identifier'].widget.attrs['readonly'] = True

    class Meta:
        model = Contracting
        fields = '__all__'
