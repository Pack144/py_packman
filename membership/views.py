from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from . import forms, models


class JoinUs(generic.CreateView):
    form_class = forms.JoinUsForm
    success_url = reverse_lazy('login')
    template_name = 'membership/join-us.html'


class MemberDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = ['assignments.view_member']
    model = models.Member
    slug_field = 'permalink'


class MemberList(PermissionRequiredMixin, generic.ListView):
    permission_required = ['assignments.view_member']
    model = models.Member


class ParentList(PermissionRequiredMixin, generic.ListView):
    permission_required = ['assignments.view_member']
    model = models.Parent


class ScoutList(PermissionRequiredMixin, generic.ListView):
    permission_required = ['assignments.view_member']
    model = models.Scout


class ContributorList(PermissionRequiredMixin, generic.ListView):
    permission_required = ['assignments.view_member']
    model = models.Contributor
