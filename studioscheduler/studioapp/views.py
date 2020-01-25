from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

#from .models import Choice, Question


def index(request):
    return HttpResponse("Hello, world. Let's schedule some studio sessions.")
