from django.shortcuts import render,redirect, get_object_or_404,reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import UserRegistrationForm,UserLoginForm,UserUpdateForm,ProfileUpdateForm
from django.http import HttpResponse

from .models import profile
from django.contrib.auth.models import User
from django.contrib import auth
# from .forms import imageform,profilecreate

from django.contrib.auth import authenticate, login





# Create your views here.

def landing_page(request):

    # auth.logout(request)
    # logout(request)
    return render(request,'users/landing_page.html')

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! Log In to continue')
            return redirect('login')
            # return redirect('home')
            
    else:
        # form = UserCreationForm()
        form = UserRegistrationForm()
    return render (request, 'users/register.html',{'form':form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/all_users.html', {'users': users})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)

        if u_form.is_valid():
            u_form.save()
            
            messages.success(request,f'Your profile has been updated!')
            return redirect('profile')
        if p_form.is_valid():
            p_form.save()
            messages.success(request,f'Your profile picture has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form':u_form,
        'p_form' : p_form
    }

    return render(request,'users/profile.html',context)


# def login(request):
#     if request.method == 'POST':
#         # form = UserCreationForm(request.POST)
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'Login successfully for {username}!')
#             # return render (request,'file_share/home.html',)
#             return redirect(reverse('home'))
#     else:
#         # form = UserCreationForm()
#         form = UserLoginForm()
#     return render (request, 'users/login.html',{'form':form})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('alreadythere')
#         else:
#             messages.info(request, 'invalid credentials')
#             return redirect('login')
#     else:
#       return render(request, 'users/login.html')

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f'Login successfully for {username}!')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
#         form = UserLoginForm()
#     return render(request, 'users/login.html', {'form': form})

# message.debug
# message.info
# message.success
# message.warning
# message.error

# def logout(request):
#     auth.logout(request)
#     return redirect('login')

# def home(request):
#     return render(request,'users/home.html')


# def register(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         print(username)
    
#         email=request.POST.get('newemail')
        
#         password1=request.POST.get('pass1')
#         print(password1)
#         password2=request.POST.get('pass2')
#         if password1 == password2:
#            if User.objects.filter(username=username).exists():
#               messages.info(request,'username taken')
#               return render(request,'users/register.html')
#            elif User.objects.filter(email=email).exists():
#               messages.info(request,'Email Taken')
#               return render(request,'users/register.html')
#            else:
#               user=User.objects.create_user(username=username,email=email,password=password1)
#               user.save()
#               return redirect('login')
#         else:
#             messages.info(request,'Password is not Matching')
#             return render(request,'users/register.html')
#     else:
#       return render(request, 'users/register.html')


# @login_required
# def alreadythere(request):
#      use=get_object_or_404(User,id=request.user.id)
#      if profile.objects.filter(owner=use).count()==0 :

#          return redirect('profile')
#      else:

#         return redirect('filesharing:home1')

# def profiles(request):
#     if request.method=='POST':
#       form=profilecreate(request.POST,request.FILES)
#       if form.is_valid():
#         g=form.save(commit=False)
#         g.owner=get_object_or_404(User,id=request.user.id)
#         p1=profile(image=g.image,profilename=g.profilename,DOB=g.DOB,college=g.college,owner=g.owner)
#         p1.save()
#         return redirect('createdprofile')


#     else:
#         form=profilecreate()
#         return render(request, 'users/profile.html',{'form':form})
# def profileupdate(request):

#     if request.method=='POST':
#       form=imageform(request.POST,request.FILES)
#       if form.is_valid():
#         g=form.save(commit=False)
#         g.owner=get_object_or_404(User,id=request.user.id)
#         p1 = profile.objects.get(owner=get_object_or_404(User,id=request.user.id))
#         DOB = p1.DOB
#         college=p1.college
#         p1.delete()
#         p1=profile(image=g.image,profilename=g.profilename,DOB=DOB,college=college,owner=g.owner)
#         p1.save()
#         return redirect('createdprofile')


#     else:
#         form=imageform()
#         return render(request, 'users/profileupdate.html',{'form':form})

# def createdprofile(request):

#     use = get_object_or_404(User, id=request.user.id)
#     p1=profile.objects.get(owner=use) 

#     return render(request,'users/createdprofile.html',{'p1':p1})

# def oprofile(request,user):
#     puser =User.objects.get(username = user)

#     p1 = profile.objects.get(owner=puser.id)

#     context = {'p1':p1}
#     return render(request,'users/oprofile.html',context)