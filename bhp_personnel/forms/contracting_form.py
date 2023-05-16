from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Contracting


class ContractingForm(SiteModelFormMixin, forms.ModelForm):

    def __init___(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contract'].widget.attrs['readonly'] = True
        self.fields['identifier'].widget.attrs['readonly'] = True

    class Meta:
        model = Contracting
        fields = '__all__'
