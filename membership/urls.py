from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberList.as_view(), name='member-list'),
    path('parents/', views.ParentList.as_view(), name='parent-list'),
    path('cubs/', views.ScoutList.as_view(), name='scout-list'),
    path('contributors/', views.ContributorList.as_view(), name='contributor-list'),
    path('join-us/', views.JoinUs.as_view(), name='join-us'),
    path('<slug:slug>/', views.MemberDetail.as_view(), name='member-detail'),
]
