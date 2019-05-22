from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from .models import Committee


class CommitteeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Committee
    slug_field = 'permalink'


class CommitteesListView(LoginRequiredMixin, generic.ListView):
    model = Committee
    paginate_by = 20
