from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
        help_text='<p>Refers to managing others through effective leadership '
                  'based on managerial expertise, provision of strategic '
                  'guidance, emotional intelligence and ability to generate'
                  ' respect; and extent to which the manager develops a team'
                  ' approach to the achievement of objectives and the '
                  'management of staff.Performance indicators include:</p>'

                  '<p>&#10003;	Encourages participation in planning and goal '
                  'setting and decision making process.<br>'
                  '&#10003;	Encourages team effectiveness through open '
                  'discussion, empowerment and consultation<br>'
                  '&#10003;	Actively seeks the opinions of others before '
                  'taking decisions; Keeps people informed of decisions and '
                  'issues particularly those which may effect their individual'
                  'areas of responsibility, Monitors work through the provision'
                  ' of positive feedback <br>'
                  '&#10003;	Acts transparently with members of the team and '
                  'addresses any failures directly, Leads by example '
                  '(i.e. provides a model for desired behaviour) and '
                  'generates respect of others<br>'
                  '&#10003;	Ability to inspire and influence through '
                  'articulation of strongly held views, Provides leadership '
                  'through active interest in the work of others with '
                  'suggestions and ideas on how work can be more effectively '
                  'performed<br>'
                  '&#10003;	Establishment and monitoring of high standards of'
                  ' performance<br></p>',
        blank=True,
        null=True)

    leadership_motivation = models.IntegerField(
        verbose_name='Team Leadership and Motivation',
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text='<h4> 1 - Rarely </br>2 - Sometimes '
                  '</br>3 - Usually </br>4 - Almost Always </br>5 - Always '
                  '</h4>')

    leadership_motivation_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'bhp_personnel'
        verbose_name = 'Team Leadership and Motivation'
        verbose_name_plural = 'Team Leadership and Motivation'
