from django.shortcuts import render, redirect
from controller.models import Job
from controller.models import JobStandby
from django.db.models import Count
from controller.models import TecnologiesInfo

def home(request):
    jobs = len(Job.objects.all())
    #jobsStandby = JobStandby.objects.all().filter(status='waiting',site='linkedin').count()
    jobsStandby = (JobStandby.objects.filter(status='waiting').values("site").annotate(Count("site")).order_by())
    jobsScrapedTerms = (Job.objects.values("researched_topic").annotate(Count("researched_topic")).order_by())
    context={'info':jobs,'standby':jobsStandby,'jobs':jobsScrapedTerms}
    return render(request, 'home/home.html',context)

def preferences(request):
    programmingLanguages = TecnologiesInfo.objects.filter(type='programming language').values("tecnologie").order_by("tecnologie").using('datasets')

    frameworks = TecnologiesInfo.objects.filter(type='framework').values("tecnologie").order_by("tecnologie").using(
        'datasets')

    database = TecnologiesInfo.objects.filter(type='database').values("tecnologie").using(
        'datasets').order_by()

    dictContext = {"languages":programmingLanguages,"frameworks":frameworks,"databases":database}
    return render(request,'preferences/preferences.html',context=dictContext)

def createPreference(request):
    from controller.models import PreferencesUser
    if request.method == 'POST':
        language = request.POST.get('programming-language')
        if language != "Select a language":
            lang = PreferencesUser(tecnologie=language,type="programming language")
            lang.save()
        framework = request.POST.get('framework')
        if framework != "Select a framework":
            framework = PreferencesUser(tecnologie=framework, type="framework")
            framework.save()
        database = request.POST.get('database')
        if database != "Select a framework":
            database = PreferencesUser(tecnologie=database, type="database")
            database.save()

        return redirect('preferences')