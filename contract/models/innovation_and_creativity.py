from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
        help_text='<p>Refers to the extent to which the employee uses critical'
                  'thinking skills to come up with creative, imaginative and '
                  'creative solutions to existing problems and obstacles and '
                  'the creation of new approaches and processes to achieve '
                  'organisational objectives and continuous improvement.</p> '
                  '<p>&#10003;	Generates new ideas and varied solutions and '
                  'approaches to overcome obstacles and maximise achievement '
                  'of desired results<br>'
                  '&#10003;	Recognises the need for new or modified '
                  'approaches and critically reviews existing processes, '
                  'procedures, etc with a view to adopt best practices and new'
                  'approaches<br>'
                  '&#10003;	Brings perspectives and approaches together '
                  'and combines them to generate creative solutions in an '
                  'imaginative manner<br>'
                  '&#10003;	Addresses complex situations and identifies '
                  'patterns and trends leading to problems and the development'
                  ' of appropriate solutions<br>'
                  '&#10003;	Exercises critical judgment based on informed '
                  'decision making and creating thinking; Anticipates potential'
                  ' impact arising out of innovations<br></p>',
        blank=True,
        null=True)

    innovation_creativity = models.IntegerField(
        verbose_name='Innovation and Creativity',
        validators=[MinValueValidator(0), MaxValueValidator(5)],)

    innovation_creativity_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    class Meta:
        app_label = 'contract'
        verbose_name = 'Innovation and Creativity'
        verbose_name_plural = 'Innovation and Creativity'
