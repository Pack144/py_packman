from django.shortcuts import render, get_object_or_404
from .models import Page


def homepage(request):
    return render(request, 'pages/home.html')


def page(request, permalink):
    page_data = get_object_or_404(Page, permalink=permalink)
    return render(request, 'pages/page.html', {'page': page_data})
