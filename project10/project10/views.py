from django.shortcuts import render
from contactEnquiry.models import contactEnquiry


def home(request):
    return render(request, "index.html")


def saveEnquiry(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        en = contactEnquiry(first_name=fname, last_name=lname, email=email)
        en.save()
    return render(request, "index.html")
