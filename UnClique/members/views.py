from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


@login_required
def home(request):
    return render(request, 'members/home.html')



def late_registration(request):
    return render(request, 'members/signup_form.html')
