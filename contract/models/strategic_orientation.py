from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class StrategicOrientation(BaseUuidModel, SiteModelMixin):

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

    strategic_orientation_desc = models.CharField(
        verbose_name='Description',
        max_length=500,
        help_text='<div style=" margin-left:-10px;"> <p><i> <b>Guidelines:</b>'
                  ' <span style="font-weight:normal;">Professional Skills Assessment helps in '
                  'identifying employees’ competencies and professional skills'
                  ' strengths and opportunities for improvement. To be '
                  'completed during the evaluation meeting with the employee.'
                  '   After discussions with the employee, put an “X” in the '
                  'box that best describes how often each skill is '
                  'demonstrated by the employee.</span><b> Make sure examples '
                  'supporting the ranking of “Always” or “Rarely” are '
                  'captured in the comments section. </b></i></p> '

                  '<p><span style="font-weight:normal; ">Refers to the provision of overall vision and guidance for '
                  'the long term success of the organisation and a desire to '
                  'maximise the organisation’s potential through a comprehensive'
                  ' understanding of the global environment in which the '
                  'organisation exists and its role and function in Botswana’s '
                  'economic, social and political development Performance '
                  'indicators include: </br>'
                  '&#10003; Establishes clear mission, goals and objectives for the '
                  'organisation </br>'
                  '&#10003; Articulates and communicates overall organisational '
                  'mission, goals and objectives, long term aims and vision of '
                  'the future </br>'
                  '&#10003;Pro-actively develops plans and strategies for the '
                  'achievement of objectives </br>'
                  '&#10003;of immediate and intermediate range goals </br>'
                  '&#10003; Thinks conceptually and holistically </br>'
                  '&#10003;Plans strategies to recognise external events'

                  '</span></p> </div>',

        blank=True,
        null=True)

    strategic_orientation = models.IntegerField(
        verbose_name='Strategic Orientation',
        blank=True,
        null=True, )

    strategic_orientation_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Strategic Orientation'
        verbose_name_plural = 'Strategic Orientation'
