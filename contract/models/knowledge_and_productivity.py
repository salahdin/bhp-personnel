from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class KnowledgeAndProductivity(BaseUuidModel, SiteModelMixin):

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

    productivity_skills_desc = models.CharField(
        verbose_name='Description',
        max_length=500,
        help_text='',
        blank=True,
        null=True)

    productivity = models.IntegerField(
        verbose_name='Job Knowledge  and productivity',
        blank=True,
        null=True,
        help_text='The extent to which the employee demonstrates a thorough '
                  'knowledge of the job based on technical/professional '
                  'principles and practices, and the ability to extrapolate '
                  'from things learned to new situations. ')

    productivity_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Knowledge And Productivity'
        verbose_name_plural = 'Knowledge And Productivity'
