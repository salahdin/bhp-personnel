from django import forms
from django.core.exceptions import ValidationError

from edc_base.sites import SiteModelFormMixin

from ..models import Employee, Supervisor


class EmployeeForm(SiteModelFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['identifier'].required = False

    identifier = forms.CharField(
        label='Employee Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        supervisor = self.cleaned_data.get('supervisor')
        supervisor_alt = self.cleaned_data.get('supervisor_alt')
        if supervisor == supervisor_alt:
            message = {
                'supervisor_alt':
                'Please select a supervisor different from the first one'}
            raise ValidationError(message)

    class Meta:
        model = Employee
        fields = '__all__'


class SupervisorForm(forms.ModelForm):

    class Meta:
        model = Supervisor
        fields = '__all__'
