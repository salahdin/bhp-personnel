from django import forms
from edc_base.sites.forms import SiteModelFormMixin

from ..models import (
    AdhereToTimeLines, FollowStandards, ProvideReports, FollowTDD,
    MaintainDocumentation, PerformSysAnalysis, ProjectAssistance,
    IntegrationAssistance, DemonstrateInterest, ReviewTeamCode,
    AssistResearchStaff, GuideJnrStaff, LeadershipSkills, AssistInManagement,
    AssistInImplementation)


class AdhereToTimeLinesForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = AdhereToTimeLines
        fields = '__all__'


class FollowStandardsForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = FollowStandards
        fields = '__all__'


class ProvideReportsForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = ProvideReports
        fields = '__all__'


class FollowTDDForm(SiteModelFormMixin, forms.ModelForm):

    class Meta:
        model = FollowTDD
        fields = '__all__'


class MaintainDocumentationForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = MaintainDocumentation
        fields = '__all__'


class PerformSysAnalysisForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = PerformSysAnalysis
        fields = '__all__'


class ProjectAssistanceForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = ProjectAssistance
        fields = '__all__'


class IntegrationAssistanceForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = IntegrationAssistance
        fields = '__all__'


class DemonstrateInterestForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = DemonstrateInterest
        fields = '__all__'


class ReviewTeamCodeForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = ReviewTeamCode
        fields = '__all__'


class AssistResearchStaffForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = AssistResearchStaff
        fields = '__all__'


class GuideJnrStaffForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = GuideJnrStaff
        fields = '__all__'


class LeadershipSkillsForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = LeadershipSkills
        fields = '__all__'


class AssistInManagementForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = AssistInManagement
        fields = '__all__'


class AssistInImplementationForm(SiteModelFormMixin, forms.ModelForm):
    class Meta:
        model = AssistInImplementation
        fields = '__all__'
