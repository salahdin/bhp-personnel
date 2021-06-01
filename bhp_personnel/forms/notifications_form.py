from django import forms

from edc_base.sites import SiteModelFormMixin

from ..models import Notifications


class NotificationsForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = Notifications
        fields = '__all__'
