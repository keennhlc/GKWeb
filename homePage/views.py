from django.shortcuts import render, get_object_or_404
from .models import HomeContent, Content


def index(request):
    news = HomeContent.objects.get(pk=1)
    slider = HomeContent.objects.get(pk=2)
    all_news = news.content_set.all()
    all_slider = slider.content_set.all()
    return render(request, 'homePage/index.html', {'all_news': all_news, 'all_slider': all_slider})


def news_detail(request, new_id):
    news = get_object_or_404(Content, pk=new_id)
    return render(request, 'homePage/details.html', {'news': news})


def slider_detail(request, slider_id):
    slider = get_object_or_404(Content, pk=slider_id)
    return render(request, 'homePage/slider.html', {'slider': slider})


"""from django.shortcuts import render, get_object_or_404
from .models import New, Slider

def index(request):
    all_news = New.objects.all()
    all_slider = Slider.objects.all()
    return render(request, 'homePage/index.html', {'all_news': all_news, 'all_slider': all_slider})


def news_detail(request, new_id):
    news = get_object_or_404(New, pk=new_id)
    return render(request, 'homePage/details.html', {'news': news})


def slider_detail(request, slider_id):
    slider = get_object_or_404(New, pk=slider_id)
    return render(request, 'homePage/sliderContent.html', {'slider': slider})"""
