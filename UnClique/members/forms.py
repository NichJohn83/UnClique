from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from members.models import member



class SignUpForm(UserCreationForm):
    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'
    FIFTH_OR_HIGHER = 'fifth+'
    GRAD = 'grad'
    FACULTY = 'faculty'
    STAFF = 'staff'
    username = forms.CharField(max_length=30, required=True, help_text='username. Will be used to sign in')
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name.')
    major = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    classification = forms.ChoiceField(choices=((
        (FIRST, 'First Year'),
        (SECOND, 'Second Year'),
        (THIRD, 'Third Year'),
        (FOURTH, 'Fourth Year'),
        (FIFTH_OR_HIGHER, 'Fifth Year or higher'),
        (GRAD, 'Graduate Student'),
        (FACULTY, 'Faculty'),
        (STAFF, 'Staff'),
    )
))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'major', 'classification', 'password1', 'password2', )

