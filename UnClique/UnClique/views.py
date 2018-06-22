from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('member_home')
    else:
        return render(request, 'unclique/welcome.html')