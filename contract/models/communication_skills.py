from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class CommunicationSkills(BaseUuidModel, SiteModelMixin):

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

    communication_skills_desc = models.CharField(
        verbose_name='Description',
        max_length=500,
        help_text='<p>Refers to the extent to which the employee demonstrates '
                  'a willingness to help others, share information to enable '
                  'them to meet their objectives and needs, communicate with '
                  'others, and inter-personal relationships.Performance '
                  'indicators include</p>'
                  '<p>&#10003;	Communicates well and responds to requests'
                  ' for information or assistance in a friendly and helpful'
                  ' manner<br>'
                  '&#10003;	Follows up enquiries promptly, Communicates '
                  'courteously and respectfully with customers and colleagues,'
                  ' Goes out of their way to help others<br>'
                  '&#10003;	Provides relevant feedback in  a timely manner'
                  ' and shares relevant  information with others<br></p>',
        blank=True,
        null=True)

    communication_skills = models.IntegerField(
        verbose_name='Communication Skills ',
        blank=True,
        null=True,
        
    )

    communication_skills_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Communication Skills'
        verbose_name_plural = 'Communication Skills'
