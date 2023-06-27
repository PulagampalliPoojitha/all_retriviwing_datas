from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q

def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(name__in=['rahul','Dhoni'])
    webpages=Webpage.objects.filter(name__regex='R\w+')
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(name='Virat') | Q(url__startswith='https'))
    webpages=Webpage.objects.filter(Q(name='Rahul') & Q(url__startswith='https'))
    
    
    
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    accessrecord=Accessrecord.objects.all()
    
    LAO=accessrecord.objects.filter(date='1995-01-18')
    LAO=accessrecord.objects.filter(date__gt='1995-01-18')
    LAO=accessrecord.objects.filter(date__lte='1995-01-18')
    LAO=accessrecord.objects.filter(date__year='2021')
    LAO=Accessrecord.objects.filter(date__month='07')
    LAO=accessrecord.objects.filter(date__day='12')
    LAO=accessrecord.objects.filter(date__year__gte='2020')
    LAO=accessrecord.objects.filter(date__year__lte='2020')
    LAO=accessrecord.objects.filter(date__day__gt='12')
    d={'accessrecord':accessrecord}
    return render(request,'display_Accessrecord.html',d)
def update_Webpage(request):
    #Webpage=Webpage.objects.filter(name='Naveen').update(url='http//www.Naveen.in')
    #Webpage=Webpage.objects.all()
    #Webpage.objects.filter(name='Naveen').update(url='http//www.Naveen.in')
    #Webpage.objects.filter(name='Thirumalesh').update(url='http//www.KTM.in')
    #Webpage.objects.filter(name='Thirumalesh').update(top_name='cricket')
    #topics=Topic.objects.get(top_name='cricket')

    #Webpage.objects.update_or_create(name='deva',defaults={'top_name':topics})
    #Webpage.objects.filter(name='Dhoni').update(url='www.dhoni.com')
   # Webpage.objects.filter(name='sachin').update(url='www.sachin.com')
    topic=Topic.objects.get(topic_name='cricket')
    Webpage.objects.update_or_create(name='Hardik',defaults={'topic_name':topic})
    webpages=Webpage.objects.all()

    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)
