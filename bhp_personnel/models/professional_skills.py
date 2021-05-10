from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .contract import Contract


class ProfessionalSkills(BaseUuidModel, SiteModelMixin):

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
                  'demonstrated by the employee.</span> <b>Make sure examples '
                  'supporting the ranking of “Always” or “Rarely” are '
                  'captured in the comments section.</b> </i></p> '
                  '<p>Refers to the provision of overall vision and guidance for '
                  'the long term success of the organisation and a desire to '
                  'maximise the organisation’s potential through a comprehensive'
                  ' understanding of the global environment in which the '
                  'organisation exists and its role and function in Botswana’s '
                  'economic, social and political development Performance '
                  'indicators include: </p>'
                  '<p>&#10003;	Establishes clear mission, goals and objectives for the '
                  'organisation </br>'
                  '&#10003;	 Articulates and communicates overall organisational '
                  'mission, goals and objectives, long term aims and vision of '
                  'the future </br>'
                  '&#10003;	Pro-actively develops plans and strategies for the '
                  'achievement of objectives </br>'
                  '&#10003;	Thinks about  the future in addition to the achievement '
                  'of immediate and intermediate range goals </br>'
                  '&#10003;	 Thinks conceptually and holistically </br>'
                  '&#10003;	 Plans strategies to recognise external events</p>'
                  '</span></h4> </div>',

        blank=True,
        null=True)

    strategic_orientation = models.IntegerField(
        verbose_name='Strategic Orientation',
        validators=[MinValueValidator(0), MaxValueValidator(5)],)

    strategic_orientation_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    results_focus = models.IntegerField(
        verbose_name='Results Focus and Commitments',
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text='Refers to the extent to which the employee is self '
                  'motivated to achieve results and continuously strives for '
                  'performance excellence through review and evaluation of '
                  'activities and identification of opportunities for '
                  'improvements and changes to enhance organisational '
                  'efficiencies and success. ')

    results_focus_comm = models.TextField(
        verbose_name='Comments on assessment:',
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

    innovation_creativity = models.IntegerField(
        verbose_name='Innovation and Creativity',
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text='Refers to the extent to which the employee uses critical '
                  'thinking skills to come up with creative, imaginative and '
                  'creative solutions to existing problems and obstacles and '
                  'the creation of new approaches and processes to achieve '
                  'organisational objectives and continuous improvement. ')

    innovation_creativity_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    planning_skills = models.IntegerField(
        verbose_name='Planning and Organising Skills',
        blank=True,
        null=True,
        help_text='Refers to the extent to which the employee demonstrates '
                  'ability to plan, organise and follow through on tasks in a '
                  'timely and effective manner. ')

    planning_skills_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    interpersonal_skills = models.IntegerField(
        verbose_name='Teamwork and Interpersonal Skills',
        blank=True,
        null=True,
        help_text='Refers to ability to function in a team environment and '
                  'to work well with others to achieve the shared work '
                  'objectives in an effective manner. ')

    interpersonal_skills_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    communication_skills = models.IntegerField(
        verbose_name='Communication Skills ',
        blank=True,
        null=True,
        help_text='Refers to the extent to which the employee demonstrates a '
                  'willingness to help others, share information to enable '
                  'them to meet their objectives and needs, communicate with '
                  'others, and inter-personal relationships')

    communication_skills_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    productivity = models.IntegerField(
        verbose_name='Job Knowledge  and productivity',
        blank=True,
        null=True,
        help_text='The extent to which the employee demonstrates a thorough '
                  'knowledge of the job based on technical/professional '
                  'principles and practices, and the ability to extrapolate '
                  'from things learned to new situations. ')

    productivity_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    quality_of_work = models.IntegerField(
        verbose_name='Quality of Work',
        blank=True,
        null=True,
        help_text='Refers to the extent to which the employee demonstrates '
                  'ability to provide accurate work free of avoidable errors.')

    quality_of_work_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    # COMPETENCIES AND PROFESSIONAL SKILLS ASSESSMENT
    def calculate_skills_assessment(self):
        score = 0
        for f in self._meta.get_fields():
            if f.name in ['strategic_orientation', 'results_focus',
                          'leadership_motivation', 'innovation_creativity',
                          'planning_skills', 'interpersonal_skills',
                          'communication_skills', 'productivity',
                          'quality_of_work', ]:
                score += int(getattr(self, f.name))
        return score

    def __str__(self):
        return f'{self.identifier}'

    class Meta:
        app_label = 'bhp_personnel'
        verbose_name = 'Competencies and professional skills ' \
                       'assessment'
        verbose_name_plural = 'Competencies and professional skills ' \
                              'assessment'
