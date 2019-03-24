from django.shortcuts import render
from .forms import ContactForm
from .models import ContactInfo
from django.contrib import messages


def contact_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
        messages.success(request, 'Form submission successful')

    context = {'form': form}
    return render(request, "contactUs/contact.html", context)
