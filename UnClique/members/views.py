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
from django.forms.models import model_to_dict



@login_required
def home(request):

    match = None
    second_match = None
    try:
        match = Member.objects.filter(email=request.user.member.current_match_email).values()[0]
    except:
        pass

    try:
        second_match = Member.objects.filter(email=request.user.member.secondary_match_email).values()[0]
    except:
        pass

    return render(request, 'members/home.html', {'match': match, 'secondary_match': second_match})



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
    list_from_string = ast.literal_eval(memberlist)
    newlist =[]
    for person in list_from_string:
        Member.objects.filter(email=person[0]['email']).update(current_match_email=person[1]['email'])
        Member.objects.filter(email=person[1]['email']).update(current_match_email=person[0]['email'])
        Member.objects.filter(email=person[0]['email']).update(secondary_match_email=None)
        Member.objects.filter(email=person[0]['email']).update(secondary_match_email=None)
        try:
            if person[2]:
                Member.objects.filter(email=person[0]['email']).update(secondary_match_email=person[2]['email'])
                Member.objects.filter(email=person[1]['email']).update(secondary_match_email=person[2]['email'])
                Member.objects.filter(email=person[2]['email']).update(secondary_match_email=person[1]['email'])
                Member.objects.filter(email=person[2]['email']).update(current_match_email=person[0]['email'])
        except IndexError:
            pass
        # newlist.append(first_person)
        # newlist.append(second_person)
        # first_person.update(current_match_email=second_person['email'])
        # second_person.update(current_match_email=first_person['email'])
    return render(request, 'members/shuffle_success.html', {'completelist': list_from_string})



def display_members(request, memberlist):
    shuffled_list = _shuffle_memebers_(memberlist)

    print('\n\n\n\n\n\n')
    print(shuffled_list)
    print('\n\n\n\n\n\n')

    return render(request, 'members/unclique_list.html', {'memberlist': list(shuffled_list)})
    # return HttpResponse(shuffled_list)


def _shuffle_memebers_(list_of_members):
    list_from_string = ast.literal_eval(list_of_members)
    shuffle(list_from_string)
    it = iter(list_from_string)
    if len(list_from_string) % 2 == 0: #if the number of participants are even
        new_list = zip(it, it)
        new_list = list(new_list)
    else: #the number of members is odd
        frontlist = []
        if len(list_from_string) > 3:
            for person in list_from_string:
                if person == list_from_string[-3]:
                    break
                frontlist.append(person)
        backlist = [list_from_string[-1], list_from_string[-2], list_from_string[-3]]
        frontit = iter(frontlist)
        backit = iter(backlist)
        new_frontlist = list(zip(frontit, frontit))
        new_backlist = list(zip(backit, backit, backit))
        new_frontlist.append(( new_backlist[0] ))
        new_list = new_frontlist


    return new_list

@login_required
def subscribe_member(request):
    Member.objects.filter(id=request.user.member.id).update(subscribed=True)
    match = Member.objects.filter(current_match_email=request.user.member.current_match_email)
    return redirect('members:member_home')


@login_required
def unsubscribe_member(request):
    Member.objects.filter(id=request.user.member.id).update(subscribed=False)
    Member.objects.filter(id=request.user.member.id).update(current_match_email=None)
    Member.objects.filter(id=request.user.member.id).update(secondary_match_email=None)
    return redirect('members:member_home')
