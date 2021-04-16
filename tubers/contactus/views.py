from django.shortcuts import redirect, render
from django.contrib import messages

from .models import ContactForm

# Create your views here.

def contactus(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']

        contactForm = ContactForm(full_name=full_name, phone=phone, email=email, company=company, subject=subject, message=message)
        contactForm.save()
        messages.success(request, 'Thanks for contacting, we will  reach you soon!!!')
        return redirect('contact')
        