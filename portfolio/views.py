# from django.shortcuts import render, redirect
# from .forms import ContactForm
# from django.contrib import messages
# from django.http import HttpResponse, HttpResponsePermanentRedirect
# from .models import Contact, Project

# def home(request):
#     return render(request, 'portfolio/index.html', {'projects': all_projects})
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # process the form data
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             # create a new Contact object with the form data
#             contact = Contact(name=name, email=email, subject=subject, message=message)
#             # save the new Contact object to the database
#             contact.save()
#             # redirect to a success page
#             messages.success(request, 'Your message has been sent. Thank you!')
#             return redirect('portfolio:home')  # or 'success' if you have defined it    
#     else:
#         form = ContactForm()
#     context = {'form': form}
#     template_name = 'portfolio/index.html'
#     return render(request, template_name, context)

# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Contact, Project

def home(request):
    all_projects = Project.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # create a new Contact object with the form data
            contact = Contact(name=name, email=email, subject=subject, message=message)
            # save the new Contact object to the database
            contact.save()
            # redirect to a success page
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('portfolio:home')  # or 'success' if you have defined it    
    else:
        form = ContactForm()
    context = {'form': form, 'projects': all_projects}
    template_name = 'portfolio/index.html'
    return render(request, template_name, context)

def projects(request):
    all_projects = Project.objects.all()
    context = {'projects': all_projects}
    template_name = 'portfolio/index.html'
    return render(request, template_name, context)
