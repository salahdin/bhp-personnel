from django.db import models

from edc_base.sites import SiteModelMixin
from edc_base.model_mixins import BaseUuidModel

from .performance_assessment import PerformanceAssessment


class PerformanceAssessmentItem(SiteModelMixin, BaseUuidModel):

    performance_assessment = models.ForeignKey(
        PerformanceAssessment,
        on_delete=models.PROTECT)

    performance_indicators = models.CharField(
        verbose_name='Key PERFORMANCE INDICATORS / MEASURES & DEADLINES '
                     '(completion dates)',
        max_length=100,)

    weighting = models.CharField(
        verbose_name='%WEIGHTING (KPA Weighting as % of total)',
        max_length=100,)

    mid_year_performance = models.CharField(
        verbose_name='Mid-Year ASSESSMENT (on Performance Results achieved)',
        max_length=100)

    kpa_rating = models.CharField(
        verbose_name='KPA RATING (Use Rating Scale)',
        max_length=100)

    kpa_score = models.CharField(
        verbose_name='KPA SCORE (Rating x Weighting)',
        max_length=100)

    year_end_assessment = models.CharField(
        verbose_name='Year- End or End of Contract  ASSESSMENT (on Performance'
                     ' Results achieved) Please circle relevant period',
        max_length=100)

    class Meta:
        abstract = True

# SECTION 3 – PERFORMANCE PLANNING & ASSESSMENT

# 1st KPA:
# Further develop and maintenance of existing clinical and laboratory
# data solutions


class AdhereToTimeLines(PerformanceAssessmentItem):

    adhere_to_timelines = models.DecimalField(
        verbose_name='Adhere to timelines set',
        decimal_places=2,
        max_digits=2)


class FollowStandards(PerformanceAssessmentItem):

    follow_standards = models.DecimalField(
        verbose_name='Follow standards that are required during the software'
                     ' development',
        decimal_places=2,
        max_digits=2)


class ProvideReports(PerformanceAssessmentItem):

    provide_reports = models.DecimalField(
        verbose_name='Provide necessary required reports from project meeting'
                     ' and project leader reports',
        decimal_places=2,
        max_digits=2)


class FollowTDD(PerformanceAssessmentItem):

    follow_tdd = models.DecimalField(
        verbose_name='Follow test driven development approach always in the '
                     'software development',
        decimal_places=2,
        max_digits=2)


class MaintainDocumentation(PerformanceAssessmentItem):

    maintain_documentation = models.DecimalField(
        verbose_name='Maintain documentation and strict source code version'
                     ' control',
        decimal_places=2,
        max_digits=2)


class PerformSysAnalysis(PerformanceAssessmentItem):

    perform_sys_analysis = models.DecimalField(
        verbose_name='Perform system analysis, requirement engineering and '
                     'design of systems',
        decimal_places=2,
        max_digits=2)


class ProjectAssistance(PerformanceAssessmentItem):

    project_assistance = models.DecimalField(
        verbose_name='Assist in project management of assigned projects as '
                     'project lead',
        decimal_places=2,
        max_digits=2)

# 2nd KPA:
# Improve integration of systems


class IntegrationAssistance(PerformanceAssessmentItem):

    integration_assistance = models.DecimalField(
        verbose_name='Assist with integration of systems such as LIS '
                     'with other systems',
        decimal_places=2,
        max_digits=2)


class DemonstrateInterest(PerformanceAssessmentItem):

    demonstrate_interest = models.DecimalField(
        verbose_name='Demonstrate interest on other systems and get '
                     'involved in customization and integration modules',
        decimal_places=2,
        max_digits=2)

# 3rd KPA:
# Quality assure software systems and participate in sites and Audits


class ReviewTeamCode(PerformanceAssessmentItem):

    review_team_code = models.DecimalField(
        verbose_name='Review team mates code and also assist in ensuring '
                     'quality software development',
        decimal_places=2,
        max_digits=2)

# 4th KPA:
# Provide good End user service and mentoring of other junior staff


class AssistResearchStaff(PerformanceAssessmentItem):

    assist_research_staff = models.DecimalField(
        verbose_name='Assist research staff with research needs that '
                     'they may have',
        decimal_places=2,
        max_digits=2)


class GuideJnrStaff(PerformanceAssessmentItem):

    guide_jnr_staff = models.DecimalField(
        verbose_name='Provide guidance to junior staff',
        decimal_places=2,
        max_digits=2)


class LeadershipSkills(PerformanceAssessmentItem):

    leadership_skills = models.DecimalField(
        verbose_name='Demonstrate leadership skills as a senior',
        decimal_places=2,
        max_digits=2)

# 5th KPA:
# Perform Data management for various projects


class AssistInManagement(PerformanceAssessmentItem):

    assist_in_management = models.DecimalField(
        verbose_name='Assist in data management of all projects managed by the'
                     ' department',
        decimal_places=2,
        max_digits=2)


class AssistInImplementation(PerformanceAssessmentItem):

    assist_in_implementation = models.DecimalField(
        verbose_name='Assist in implementation of data management plans,'
                     ' and processes.',
        decimal_places=2,
        max_digits=2)
