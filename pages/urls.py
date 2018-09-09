from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('history/', views.history_page, name='history_page'),
    path('<slug:permalink>/', views.dynamic_page, name='dynamic_page'),
]
