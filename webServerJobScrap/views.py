from django.shortcuts import render, redirect
from controller.models import Job
from controller.models import JobStandby
from django.db.models import Count

def home(request):
    jobs = len(Job.objects.all())
    jobsStandby = JobStandby.objects.all().filter(status='waiting').count()
    jobsScrapedTerms = (Job.objects.values("researched_topic").annotate(Count("researched_topic")).order_by())
    context={'info':jobs,'standby':jobsStandby,'jobs':jobsScrapedTerms}
    return render(request, 'home/home.html',context)