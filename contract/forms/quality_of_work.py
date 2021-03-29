from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import QualityOfWork


class QualityOfWorkForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = QualityOfWork
        fields = '__all__'
