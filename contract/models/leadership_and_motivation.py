from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class LeadershipAndMotivation(BaseUuidModel, SiteModelMixin):

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

    leadership_motivation_desc = models.CharField(
        verbose_name='Description',
        max_length=500,
        help_text='',
        blank=True,
        null=True)

    leadership_motivation = models.IntegerField(
        verbose_name='Team Leadership and Motivation',
        blank=True,
        null=True,
        help_text='Refers to managing others through effective leadership '
                  'based on managerial expertise, provision of strategic '
                  'guidance, emotional intelligence and ability to generate'
                  ' respect; and extent to which the manager develops a team'
                  ' approach to the achievement of objectives and the '
                  'management of staff. ')

    leadership_motivation_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Team Leadership and Motivation'
        verbose_name_plural = 'Team Leadership and Motivation'
