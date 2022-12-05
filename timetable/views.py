import datetime

from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from . models import *
from datetime import datetime
from datetime import timedelta
import datetime
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'Index.html')


def list_qualification(request):
    qualifications = Qualification.objects.all()
    context={
        'qualifications': qualifications
    }


    return render(request, 'qualification.html',context)

def qualification(request):
    if request.method =="GET" :
        qualification=request.GET.get('qualification')
        html_test= requests.get(f'https://training.gov.au/Training/Details/{qualification}').text
        soup=BeautifulSoup(html_test, 'lxml')
        Usage_recommendation=soup.find('div', class_='display-field')
        #mapping=soup.find('div', class_='display-field-info')

        #print(Usage_recommendation)
    return render(request, 'quali.html')



def timetable(request,national_code):

    dates = Units.objects.filter(qualification__national_code = national_code)
    count = Units.objects.filter(qualification__national_code = national_code).count()
    qualif=Qualification.objects.all(national_code =  national_code)
    for qualify in qualif:
        unit_start=qualify.start_date


    startdate=[]
    enddate = []
    assignmentdate = []
    classhour=[]



    for date in dates:

        start_date =unit_start
        end_date = unit_start + timedelta(weeks=date.duration) - timedelta(days=1)
        assignment_date =unit_start + timedelta(weeks=date.duration) - timedelta(days=1) +  timedelta(days=14)
        assignment = assignment_date.strftime("%d-%b-%Y")
        end = end_date.strftime("%d-%b-%Y")
        enddate.append(end)
        assignmentdate.append(assignment)
        class_hour = date.duration * 20
        classhour.append(class_hour)
















    context={
        'dates': dates,
        'end': enddate,
        'assignmentdate' : assignmentdate,
        'classhour': classhour





    }
    return render(request, 'timetable.html',context)
