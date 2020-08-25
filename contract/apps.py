from django.apps import AppConfig as DjangoAppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class AppConfig(DjangoAppConfig):
    name = 'contract'
    verbose_name = 'Contract Management'
    admin_site_name = 'contract_admin'
    identifier_pattern = None


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Contract Management System'
    institution = 'Botswana-Harvard AIDS Institute'
