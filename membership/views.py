from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import WebsiteLoginCreationForm
from .models import Member


class JoinUs(generic.CreateView):
    form_class = WebsiteLoginCreationForm
    success_url = reverse_lazy('login')
    template_name = 'membership/join-us.html'


class MemberDetail(PermissionRequiredMixin, generic.DetailView):
    permission_required = ['assignments.view_member']
    model = Member
    slug_field = 'permalink'


class MemberList(PermissionRequiredMixin, generic.ListView):
    permission_required = ['assignments.view_member']
    model = Member
