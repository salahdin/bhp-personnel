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
        help_text='<p>Refers to ability to function in a team environment and '
                  'to work well with others to achieve the shared work '
                  'objectives in an effective manner.Performance indicators '
                  'include:</p> <p>&#10003;	Participation in the planning and '
                  'goal setting and decision making process.<br>'
                  '&#10003;	Participation in open discussions, high willingness'
                  ' to share information and ability to seek the opinions of '
                  'others and providing relevant feedback<br>'
                  '&#10003;	Cooperates and works well with others, is flexible,'
                  ' adaptable and accepts constructive criticism and shows '
                  'interest in improving work performance<br>'
                  '&#10003;	Promotes group goals, has positive impact on '
                  'the group, is diligent and approaches conflict in a '
                  'constructive, professional manner.<br>'
                  '&#10003;	Relates with others in an open, friendly and '
                  'accepting manner, shows sincere interest and concern for '
                  'others, listens openly and encourages others to express '
                  'their opinions and ideas<br></p>',
        blank=True,
        null=True)

    interpersonal_skills = models.IntegerField(
        verbose_name='Teamwork and Interpersonal Skills',
        blank=True,
        null=True,
        
    )

    interpersonal_skills_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Teamwork and Interpersonal Skills'
        verbose_name_plural = 'Teamwork and Interpersonal Skills'
