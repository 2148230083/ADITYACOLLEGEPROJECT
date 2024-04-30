# from django.contrib import admin
from django.urls import path
from Greenworld.views import *

urlpatterns =[
    path('',home,name='home'),

]