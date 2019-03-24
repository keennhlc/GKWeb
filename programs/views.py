from django.shortcuts import render, get_object_or_404
from .models import Program


def index(request):
    all_programs = Program.objects.all()
    return render(request, 'programs/program.html', {'all_programs': all_programs})


def detail(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request, 'Programs/detail.html', {'program': program})


