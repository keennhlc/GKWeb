from django.shortcuts import render
from .models import Admission


def index(request):
    all_admission = Admission.objects.all()
    return render(request, 'admissions/index.html', {'all_admission': all_admission})
