from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpages(request):
    LWO = Webpage.objects.all()
    s={'LWO': LWO }
    return render(request,'display_webpages.html',s)

def display_access(request):
    LAO = AccsesRecord.objects.all()
    t={'LAO': LAO }
    return render(request,'display_access.html',t)