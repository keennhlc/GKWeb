from django import forms

from .models import ContactInfo


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'gender', 'previous_schooling', 'contact_number', 'email', 'interested_course', 'comment']
