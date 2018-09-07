from django.shortcuts import render, get_object_or_404
from .models import Page


def about_page(request):
    return render(request, 'pages/about.html')


def history_page(request):
    return render(request, 'pages/history.html')


def home_page(request):
    return render(request, 'pages/home.html')


def dynamic_page(request, permalink):
    page_data = get_object_or_404(Page, permalink=permalink)
    return render(request, 'pages/page.html', {'dynamic_page': page_data})
