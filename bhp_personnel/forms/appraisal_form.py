from django import forms
from django.core.exceptions import ValidationError
from django.apps import apps as django_apps
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidator, FormValidatorMixin

from ..models import Appraisal


class AppraisalFormValidator(FormValidator):

    def clean(self):
        super().clean()
        supervisor_signature = self.cleaned_data.get('supervisor_signature')
        employee_signature = self.cleaned_data.get('employee_signature')

        emp_identifier = self.cleaned_data.get('emp_identifier')
        employee_cls = django_apps.get_model('bhp_personnel.employee')

        try:
            employee = employee_cls.objects.get(identifier=emp_identifier)
        except employee_cls.DoesNotExist:
            message = {'supervisor_signature': "Employee not found for the provided identifier."}
            self._errors.update(message)
            raise ValidationError(message)

        supervisor_full_name = f"{employee.supervisor.first_name} {employee.supervisor.last_name}"
        employee_full_name = f"{employee.first_name} {employee.last_name}"

        if supervisor_full_name != supervisor_signature:
            message = {'supervisor_signature': "The provided supervisor signature is incorrect."
                                               " Please enter the supervisor's full name (first name and last name)"
                                               " as the signature."}
            self._errors.update(message)
            raise ValidationError(message)

        if employee_signature != employee_full_name:
            message = {'employee_signature': "The provided employee signature is incorrect."
                                             " Please enter the employee's full name (first name and last name)"
                                             " as the signature."}
            self._errors.update(message)
            raise ValidationError(message)


class AppraisalForm(FormValidatorMixin, SiteModelFormMixin, forms.ModelForm):
    form_validator_cls = AppraisalFormValidator
    emp_identifier = forms.CharField(
        label='Employee ID',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    assessment_type = forms.CharField(
        label='Assessment Type',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Appraisal
        fields = '__all__'
