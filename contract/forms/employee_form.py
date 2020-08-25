from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Employee


class EmployeeForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
