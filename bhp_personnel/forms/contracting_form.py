from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Contracting


class ContractingForm(SiteModelFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contract'].disabled = True
        self.fields['identifier'].disabled = True

    class Meta:
        model = Contracting
        fields = '__all__'
