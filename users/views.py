from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from.forms import UserRegistrationForm

# Create your views here.

def landing_page(request):
    return render(request,'users/landing_page.html')

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('home')
    else:
        # form = UserCreationForm()
        form = UserRegistrationForm()
    return render (request, 'users/register.html',{'form':form})


# message.debug
# message.info
# message.success
# message.warning
# message.error