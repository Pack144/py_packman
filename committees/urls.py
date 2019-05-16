from django.urls import path
from .views import CommitteeDetailView, CommitteesListView

urlpatterns = [
    path('', CommitteesListView.as_view(), name='committees-list'),
    path('<str:slug>/', CommitteeDetailView.as_view(), name='committee-detail'),
]
