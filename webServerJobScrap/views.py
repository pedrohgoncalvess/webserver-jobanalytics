from django.shortcuts import render, redirect
from controller.models import Job
from controller.models import JobStandby
from django.db.models import Count
from controller.models import TecnologiesInfo
from controller.models import AnalyticDescription

def home(request):
    jobs = len(Job.objects.all())

    jobsStandby = (JobStandby.objects.filter(status='waiting').values("site").annotate(Count("site")).order_by())
    jobsScrapedTerms = (Job.objects.values("researched_topic").annotate(Count("researched_topic")).order_by("-researched_topic__count"))

    ProgrammingLang = (AnalyticDescription.objects.filter(type='programming language').values("info").annotate(Count("info")).using('analytic').order_by('-info__count'))

    Frameworks = (
        AnalyticDescription.objects.filter(type='framework').values("info").annotate(Count("info")).using(
            'analytic').order_by('-info__count'))

    termListProg = []
    countListProg = []

    termListFram = []
    countListFram = []

    for dictTerm in ProgrammingLang:
        if len(termListProg) < 5:
            if dictTerm.get("info") !=  'r':
                termListProg.append(dictTerm.get("info").upper())
                countListProg.append(dictTerm.get("info__count"))

    for dictTerm in Frameworks:
        if len(termListFram) < 5:
            termListFram.append(dictTerm.get("info").upper())
            countListFram.append(dictTerm.get("info__count"))

    context={'info':jobs,'standby':jobsStandby,'jobs':jobsScrapedTerms,"dataProg":countListProg,"labelProg":termListProg,"dataFram":countListFram,"labelFram":termListFram}
    return render(request, 'home/home.html',context)