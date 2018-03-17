from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from coddy.forms import *
from coddy.models import *
import time
# Create your views here.


def main_site(request):
    Vols = Vol.objects.filter()
    return render(request, "main.html", locals())


def main_site_en(request):
    Vols = Vol.objects.filter()
    return render(request, "main_en.html", locals())


def donate(request):
    form = DonateForm()
    if request.method == "POST":
        form = DonateForm(request.POST)
        if 'send' in request.POST.keys() and request.POST['send']:
            if form.is_valid():
                form.save()
                time.sleep(3)
                return redirect("main")
    return render(request, "donate.html", locals())


def donate_en(request):
    form = DonateForm()
    if request.method == "POST":
        form = DonateForm(request.POST)
        if 'send' in request.POST.keys() and request.POST['send']:
            if form.is_valid():
                form.save()
                time.sleep(3)
                return redirect("main_en")
    return render(request, "donate_en.html", locals())

def volunteer(request):
    form = VolunteerForm()
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if 'send' in request.POST.keys() and request.POST['send']:
            if form.is_valid():
                form.save()
                time.sleep(3)
                return redirect("main")
    return render(request, "volunteer.html", locals())


def volunteer_en(request):
    form = VolunteerForm()
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if 'send' in request.POST.keys() and request.POST['send']:
            if form.is_valid():
                form.save()
                time.sleep(3)
                return redirect("main_en")
    return render(request, "volunteer_en.html", locals())
