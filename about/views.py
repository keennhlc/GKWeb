from django.shortcuts import render
from .models import AboutData


def index(request):
    all_data = AboutData.objects.all()
    return render(request, 'about/index.html', {'all_data': all_data})
