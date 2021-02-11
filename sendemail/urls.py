from django.contrib import admin
from django.urls import path

from .views import submitemailaddress, successView, contactView

urlpatterns = [
    path('contact/', submitemailaddress, name='contact'),
    path('success/', successView, name='success'),
]
