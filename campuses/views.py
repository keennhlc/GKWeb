from django.shortcuts import render, get_object_or_404
from .models import Campus


def index(request):
    all_campus = Campus.objects.all()
    return render(request, 'campuses/index.html', {'all_campus': all_campus})


def detail(request, campus_id):
    campus = get_object_or_404(Campus, pk=campus_id)
    return render(request, 'campuses/detail.html', {'campus': campus})

