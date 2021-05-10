from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
        help_text='<p>The extent to which the employee demonstrates a thorough'
                  'knowledge of the job based on technical/professional '
                  'principles and practices, and the ability to extrapolate '
                  'from things learned to new situations.Performance indicators'
                  ' include:</p> '
                  '<p>&#10003;	Excellent familiarity with duties and '
                  'responsibilities, terminology, equipment (Lab equipment,PCs'
                  ', Office Systems etc)<br>'
                  '&#10003;	Application of knowledge to the work and '
                  'understanding of processes, principles and procedures<br>'
                  '&#10003;	Applications of technical know-how in the '
                  'completion of work and solving problems; Willingness '
                  'to share technical knowledge with others<br>'
                  '&#10003;	Knowledge of related tasks and functions needed '
                  'to carry out assigned duties; Minimise errors arising out '
                  'of misapplication or lack of knowledge<br>'
                  '&#10003;	Does not constantly seek assistance in areas where'
                  'knowledge is expected; Self confidence in application of '
                  'knowledge<br>'
                  '&#10003;	Ability to apply knowledge to unique situations; '
                  'Diagnosis of problems using technical knowledge<br>'
                  '&#10003;	Ability to complete appropriate work volumes and '
                  'achieve results in a timely manner, responsiveness to '
                  'deadlines<br></p>',
        blank=True,
        null=True)

    productivity = models.IntegerField(
        verbose_name='Job Knowledge  and productivity',
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text='<h4> 1 - Rarely </br>2 - Sometimes '
                  '</br>3 - Usually </br>4 - Almost Always </br>5 - Always '
                  '</h4>')

    productivity_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'bhp_personnel'
        verbose_name = 'Knowledge And Productivity'
        verbose_name_plural = 'Knowledge And Productivity'
