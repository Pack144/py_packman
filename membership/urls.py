from django.conf.urls import url
from django.urls import path
from django.views.generic.base import TemplateView

from django_registration.backends.activation.views import ActivationView, RegistrationView

from . import forms, views

urlpatterns = [
    path('', views.MemberList.as_view(), name='member-list'),
    path('parents/', views.ParentList.as_view(), name='parent-list'),
    path('cubs/', views.ScoutList.as_view(), name='scout-list'),
    path('contributors/', views.ContributorList.as_view(), name='contributor-list'),
    path('register/', RegistrationView.as_view(form_class=forms.RegistrationForm), name='register'),
    path('<slug:slug>/', views.MemberDetail.as_view(), name='member-detail'),

    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='django_registration/activation_complete.html'
        ),
        name='django_registration_activation_complete'),
    # The activation key can make use of any character from the
    # URL-safe base64 alphabet, plus the colon as a separator.
    url(r'^activate/(?P<activation_key>[-:\w]+)/$',
        ActivationView.as_view(),
        name='django_registration_activate'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='django_registration/registration_complete.html'
        ),
        name='django_registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='django_registration/registration_closed.html'
        ),
        name='django_registration_disallowed'),
]
