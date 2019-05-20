from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import WebsiteLoginCreationForm
from .models import Member


class JoinUs(generic.CreateView):
    form_class = WebsiteLoginCreationForm
    success_url = reverse_lazy('login')
    template_name = 'membership/join-us.html'


class MemberDetail(LoginRequiredMixin, generic.DetailView):
    model = Member
    slug_field = 'permalink'

