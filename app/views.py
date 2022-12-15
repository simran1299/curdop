from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *

def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpages(request):
    LWO = Webpage.objects.all() 
    LWO = Webpage.objects.filter(topic_name='football') 
    LWO=Webpage.objects.exclude(topic_name='cricket')
    LWO=Webpage.objects.all()[2:5:]
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.filter(topic_name='cricket').order_by('-name')
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
    s={'LWO': LWO }
    return render(request,'display_webpages.html',s)

def display_access(request):
    LAO = AccsesRecord.objects.all()
    t={'LAO': LAO }
    return render(request,'display_access.html',t)