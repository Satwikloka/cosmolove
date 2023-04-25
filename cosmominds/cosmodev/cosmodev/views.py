from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView


class IndexViewPage(TemplateView):
    template_name ='index.html'

   


