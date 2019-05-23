from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberList.as_view(), name='members-list'),
    path('join-us/', views.JoinUs.as_view(), name='join-us'),
    path('<slug:slug>/', views.MemberDetail.as_view(), name='member-detail'),
]
