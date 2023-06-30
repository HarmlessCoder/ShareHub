from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author' : 'gautam',
        'title' : 'File 1',
        'content' : 'First file',
        'date_posted' : 'Aug 27,2018'
    },
    {
        'author' : 'nikhil',
        'title' : 'File 2',
        'content' : 'Second file',
        'date_posted' : 'Aug 28,2018'
    }
]

def landing_page(request):
    return render(request,'file_share/landing_page.html')

def home(request):
    context={
        'posts': posts
    }
    return render(request,'file_share/home.html',context)

def about(request):
    return render(request,'file_share/about.html',{'title':'About'})

