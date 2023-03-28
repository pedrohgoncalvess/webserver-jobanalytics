from django.shortcuts import render, redirect
from controller.models import Job
from controller.models import JobStandby
from django.db.models import Count
from controller.models import TecnologiesInfo

def home(request):
    jobs = len(Job.objects.all())

    jobsStandby = (JobStandby.objects.filter(status='waiting').values("site").annotate(Count("site")).order_by())
    jobsScrapedTerms = (Job.objects.values("researched_topic").annotate(Count("researched_topic")).order_by("-researched_topic__count"))

    termList = []
    countList = []

    for dictTerm in jobsScrapedTerms:
        if len(termList) < 5:
            termList.append(dictTerm.get("researched_topic"))
            countList.append(dictTerm.get("researched_topic__count"))



    context={'info':jobs,'standby':jobsStandby,'jobs':jobsScrapedTerms,"data":countList,"label":termList}
    return render(request, 'home/home.html',context)