from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class UserLoginForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','password1']

class imageform(forms.ModelForm):

    class Meta:
        model = profile
        fields = ('image','profilename', )

class profilecreate(forms.ModelForm):

    class Meta:
        model = profile
        fields = ('image','profilename','DOB','college' )
