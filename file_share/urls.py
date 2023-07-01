from django.urls import path
from . import views

urlpatterns = [
    # path('', views.landing_page,name='landing_page'),
    path('about/', views.about,name='About'),
    path('', views.home,name='home'),
]