from django.urls import reverse_lazy
from django.views import generic

from .forms import WebsiteLoginCreationForm
from .models import Member


class JoinUs(generic.CreateView):
    form_class = WebsiteLoginCreationForm
    success_url = reverse_lazy('login')
    template_name = 'members/join-us.html'


class MemberDetail(generic.DetailView):
    model = Member
    template_name = 'members/member_detail.html'
