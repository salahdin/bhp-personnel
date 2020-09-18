from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Department


class DepartmentForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = Department
        fields = '__all__'
