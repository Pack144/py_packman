from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from .models import Committee, Den


class CommitteeDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = ['assignments.view_committee']
    model = Committee
    slug_field = 'permalink'


class CommitteesListView(PermissionRequiredMixin, generic.ListView):
    permission_required = ['assignments.view_committee']
    model = Committee
    paginate_by = 20


class DenDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = ['assignments.view_den']
    model = Den
    slug_field = 'permalink'


class DenListView(PermissionRequiredMixin, generic.ListView):
    permission_required = ['assignments.view_den']
    model = Den
    paginate_by = 20
