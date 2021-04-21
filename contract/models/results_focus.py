from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class ResultsFocus(BaseUuidModel, SiteModelMixin):

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

    results_focus_desc = models.CharField(
        verbose_name='Description',
        help_text='<p>Refers to the extent to which the employee is self '
                  'motivated to achieve results and continuously strives for '
                  'performance excellence through review and evaluation of '
                  'activities and identification of opportunities for '
                  'improvements and changes to enhance organisational '
                  'efficiencies and success.Performane indecators include: '
                  '</p> <p>&#10003;	Continuously strives to achieve and exceed'
                  ' standards of performance<br> &#10003;	Expresses concern'
                  ' about organisational inefficiencies and waste, Establishes'
                  ' personal goals and standards to ensure achievement of '
                  'objectives<br> &#10003;	Within level of authority and '
                  'accountability identifies and implements changes in '
                  'working methods to improve performance, out-put, customer'
                  ' service, etc<br> &#10003;	Pro-actively seeks to '
                  'cooperate with others and jointly achieve organisational '
                  'success<br> &#10003;	Concentrates on activities which add '
                  'value, contribute to achievement of objectives, Is prepared'
                  ' to put organisational objectives ahead of individual goals'
                  ' where necessary, Develops strategies and plans to best '
                  'achieve objectives<br> &#10003;	Identifies resource needs '
                  'and prioritises allocation of resources, Reviews and '
                  'assesses achievements against strategic objectives, '
                  'Articulates and communicates strategies and plans to '
                  'staff<br> &#10003;	Anticipates impact of future events '
                  'on strategies and plans and achievement of immediate and '
                  'intermediate range goals, Thinks conceptually and '
                  'holistically</p>',
        max_length=500,
        blank=True,
        null=True)

    results_focus = models.CharField(
        verbose_name='Results Focus and Commitments',
        max_length=500)

    results_focus_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Results Focus and Commitments'
        verbose_name_plural = 'Results Focus and Commitments'
