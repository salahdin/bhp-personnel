from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class InterpersonalSkills(BaseUuidModel, SiteModelMixin):

    emp_identifier = models.CharField(
        verbose_name="Employee Identifier",
        max_length=36,
        null=True,
        blank=True)

    contract = models.ForeignKey(
        Contract,
        on_delete=models.PROTECT,
        blank=True,
        null=True)

    # SECTION 4 – COMPETENCIES AND PROFESSIONAL SKILLS ASSESSMENT

    interpersonal_skills_desc = models.CharField(
        verbose_name='Description',
        max_length=500,
        help_text='',
        blank=True,
        null=True)

    interpersonal_skills = models.IntegerField(
        verbose_name='Teamwork and Interpersonal Skills',
        blank=True,
        null=True,
        help_text='Refers to ability to function in a team environment and '
                  'to work well with others to achieve the shared work '
                  'objectives in an effective manner. ')

    interpersonal_skills_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Teamwork and Interpersonal Skills'
        verbose_name_plural = 'Teamwork and Interpersonal Skills'
