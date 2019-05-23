from django.urls import path
from .views import CommitteeDetailView, CommitteesListView, DenDetailView, DenListView

urlpatterns = [
    path('committees/', CommitteesListView.as_view(), name='committees-list'),
    path('committee/<str:slug>/', CommitteeDetailView.as_view(), name='committee-detail'),
    path('dens/', DenListView.as_view(), name='dens-list'),
    path('den/<int:pk>', DenDetailView.as_view(), name='den-detail'),
]
