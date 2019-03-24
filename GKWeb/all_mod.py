from programs.models import Program
from homePage.models import HomeContent
from campuses.models import Campus


def program_nav(request):
    pn = Program.objects.all()
    return {'pn': pn}


def home_nav(request):
    hn = HomeContent.objects.all()
    return {'hn': hn}


def campus_nav(request):
    cn = Campus.objects.all()
    return {'cn': cn}
