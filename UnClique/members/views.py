from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from members.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'members/home.html')



def late_registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.member.preferred_name = form.cleaned_data.get('preferred_name')
            user.member.first_name = form.cleaned_data.get('first_name')
            user.member.last_name = form.cleaned_data.get('last_name')
            user.member.email = form.cleaned_data.get('email')
            user.member.classification = form.cleaned_data.get('classification')
            user.member.major = form.cleaned_data.get('major')
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('member_home')
    else:
        form = SignUpForm()

    return render(request, 'members/signup_form.html', {'form': form})
