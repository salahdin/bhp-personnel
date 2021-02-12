from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin

from .employee import Employee


class PerformanceAssessment(BaseUuidModel, SiteModelMixin):

    identifier = models.CharField(
        verbose_name="Employee Identifier",
        max_length=36,
        null=True,
        blank=True)

    employee = models.ForeignKey(Employee,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)

    # period_covered = models.CharField(
    #     verbose_name='Period Covered',)

    period_covered = models.CharField(
        verbose_name='Review Dates',
        max_length=200,
        blank=True,
        null=True)

    mid_year_review = models.DateField()

    year_end_review = models.DateField()

    contract_end_review = models.DateField()

    agreed_by = models.CharField(
        verbose_name='Agreed By',
        max_length=30)

    supervisor_signature = models.CharField(
        max_length=25
    )

    date_supervisor_signed = models.DateField()

    employee_signature = models.CharField(
        max_length=25
    )

    date_employee_signed = models.DateField()

    approved_by = models.CharField(
        verbose_name='Approved By',
        max_length=200,
        blank=False,
        null=False)

    signature = models.CharField(
        max_length=25)

    date = models.DateField()

    # SECTION 4 – COMPETENCIES AND PROFESSIONAL SKILLS ASSESSMENT

    strategic_orientation = models.IntegerField(
        verbose_name='Strategic Orientation',
        blank=True,
        null=True,
        help_text='Refers to the provision of overall vision and guidance for'
                  ' the long term success of the organisation and a desire to '
                  'maximise the organisation’s potential through a '
                  'comprehensive understanding of the global environment in '
                  'which the organisation exists and its role and function in '
                  'Botswana’s economic, social and political development. ')

    strategic_orientation_comm = models.TextField(
        verbose_name='Comments on assessment:',
        blank=True,
        null=True)

    results_focus = models.IntegerField(
        verbose_name='Results Focus and Commitments',
        max_length=200,
        blank=True,
        null=True,
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
        blank=True,
        null=True,
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

    overall_perf_score = models.IntegerField(
        verbose_name='Overall Performance Score',
        blank=True,
        null=True)

    comp_nd_pro_score = models.IntegerField(
        verbose_name='Overall Competencies & Professional Skills Score',
        blank=True,
        null=True)

    final_assess_score = models.IntegerField(
        verbose_name='Final Assessment Score (Add the weighted scores)',
        blank=True,
        null=True)

    emp_comments = models.TextField(
        verbose_name='Comments by employee',
        blank=True,
        null=True)

    supervisor_comments = models.TextField(
        verbose_name='Comments by supervisor',
        blank=True,
        null=True)

    emp_name = models.CharField(
        verbose_name='Employee\'s Name',
        max_length=30,)

    manager = models.CharField(
        verbose_name='Manager / Study Coordinator / Director / Executive / '
                     'Head of Department:  ',
        max_length=30,)

    manager_signature = models.CharField(
        verbose_name='Manager\'s signature',
        max_length=35)

    date_manager_signed = models.CharField(
        verbose_name='Date manager signed',
        max_length=35)

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
        app_label = 'contract'
        verbose_name = 'Performance Assessment'
        verbose_name_plural = 'Performance Assessment'
