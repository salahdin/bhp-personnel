from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class PlanningSkills(BaseUuidModel, SiteModelMixin):

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

    planning_skills_desc = models.CharField(
        verbose_name='Description',
        max_length=500,
        help_text='<p>Refers to the extent to which the employee demonstrates '
                  'ability to plan, organise and follow through on tasks in a '
                  'timely and effective manner.Paerformance indicators i'
                  'nclude: </p> '
                  '<p>&#10003;	Sets priorities to meet deadlines according '
                  'to work Plan<br>'
                  '&#10003;	Anticipates and responds to changes in the work '
                  'environment and takes appropriate action to ensure '
                  'achievement of required results<br>'
                  '&#10003;	Identifies resources and prioritises allocation'
                  ' of resources in accordance with the strategic requirements'
                  '<br></p>',
        blank=True,
        null=True)

    planning_skills = models.IntegerField(
        verbose_name='Planning and Organising Skills',
        validators=[MinValueValidator(0), MaxValueValidator(5)],)

    planning_skills_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Planning And Organising Skills'
        verbose_name_plural = 'Planning And Organising Skills'
