from django.contrib import admin
from django.urls import path
from version2020 import views
urlpatterns = [
    path("",views.index,name='home'),
    path('events',views.events,name='events'),
    path("teams",views.teams,name='teams'),
    path("contactus",views.contactus,name='contactus'),
    
    path("gallery",views.gallery,name='gallery'),
    
    path("testkp",views.testkp,name='testkp'),
    path("new",views.new,name='new'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("register",views.register,name='register'),
    path("home",views.index,name='home'),
    path("hometest",views.hometest,name='hometest'),

    
    path("registerwithimg",views.registerwithimg,name='registerwithimg'),
    
    
]