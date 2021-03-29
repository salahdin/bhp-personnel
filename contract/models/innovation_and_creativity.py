from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class InnovationAndCreativity(BaseUuidModel, SiteModelMixin):

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

    innovation_creativity_desc = models.CharField(
        verbose_name='Description',
        max_length=500,
        help_text='',
        blank=True,
        null=True)

    innovation_creativity = models.CharField(
        verbose_name='Innovation and Creativity',
        max_length=500,
        blank=True,
        null=True,
        help_text='Refers to the extent to which the employee uses critical '
                  'thinking skills to come up with creative, imaginative and '
                  'creative solutions to existing problems and obstacles and '
                  'the creation of new approaches and processes to achieve '
                  'organisational objectives and continuous improvement. ')

    innovation_creativity_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Innovation and Creativity'
        verbose_name_plural = 'Innovation and Creativity'
