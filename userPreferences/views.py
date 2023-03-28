from django.shortcuts import render, redirect
from controller.models import Job
from controller.models import JobStandby
from django.db.models import Count
from controller.models import TecnologiesInfo
from userPreferences.models import PreferencesUser

def preferences(request):
    programmingLanguages = TecnologiesInfo.objects.filter(type='programming language').values("tecnologie").order_by("tecnologie").using('datasets')

    frameworks = TecnologiesInfo.objects.filter(type='framework').values("tecnologie").order_by("tecnologie").using(
        'datasets')

    database = TecnologiesInfo.objects.filter(type='database').values("tecnologie").using(
        'datasets').order_by()

    preferTec = PreferencesUser.objects.all().order_by("tecnologie")


    dictContext = {"languages":programmingLanguages,"frameworks":frameworks,"databases":database,"tecnologiesPref":preferTec}
    return render(request, 'preferences/preferences.html', context=dictContext)

def createPreference(request):
    from userPreferences.models import PreferencesUser
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
        if database != "Select a database":
            database = PreferencesUser(tecnologie=database, type="database")
            database.save()

        return redirect('home-preferences')

def excludePreference(request,id):
    deletePref = PreferencesUser.objects.get(id=id)
    deletePref.delete()
    return redirect('home-preferences')
