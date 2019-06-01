from django.shortcuts import render, get_object_or_404

from . import models


def home_page(request):
    try:
        page_content = models.StaticPage.objects.get(page='H')
    except:
        page_content = None
    context = {'page_content': page_content}
    return render(request, 'pages/home.html', context)


def about_page(request):
    try:
        page_content = models.StaticPage.objects.get(page='A')
    except:
        page_content = None
    context = {'page_content': page_content}
    return render(request, 'pages/about.html', context)


def history_page(request):
    try:
        page_content = models.StaticPage.objects.get(page='L')
    except:
        page_content = None
    context = {'page_content': page_content}
    return render(request, 'pages/history.html', context)


def dynamic_page(request, permalink):
    page_data = get_object_or_404(models.DynamicPage, permalink=permalink)
    return render(request, 'pages/page.html', {'dynamic_page': page_data})
