from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Email

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            email=Email()
            email.email= request.POST.get('email')
            email.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))





def submitemailaddress(request):
        if request.method == 'POST':
            if request.POST.get('email'):
                email=Email()
                email.email= request.POST.get('email')
                email.save()

                return render(request, 'success.html')

        else:
                return render(request,'_partial.html')
