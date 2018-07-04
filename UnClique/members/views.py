import simplejson
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import ast
from random import shuffle
# Create your views here.
from members.forms import SignUpForm
from members.models import Member


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
            return redirect('members:member_home')
    else:
        form = SignUpForm()

    return render(request, 'members/signup_form.html', {'form': form})


def graduation(request, memberlist):
    # Functionality to actually persist the pairings in the DB go here

    return render(request, 'members/shuffle_success.html', {'completelist': memberlist})



def display_members(request, memberlist):
    shuffled_list = _shuffle_memebers_(memberlist)

    return render(request, 'members/unclique_list.html', {'memberlist': list(shuffled_list)})
    # return HttpResponse(shuffled_list)


def _shuffle_memebers_(list_of_members):
    list_from_string = ast.literal_eval(list_of_members)
    shuffle(list_from_string)
    it = iter(list_from_string)
    new_list = zip(it, it)
    return new_list

@login_required
def subscribe_member(request):
    Member.objects.filter(id=request.user.member.id).update(subscribed=True)
    return redirect('members:member_home')


@login_required
def unsubscribe_member(request):
    Member.objects.filter(id=request.user.member.id).update(subscribed=False)
    return redirect('members:member_home')
