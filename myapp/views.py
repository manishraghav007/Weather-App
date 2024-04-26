from django.shortcuts import render
from myapp.forms import ReportForm
from django.http import HttpResponse

from .models import Report
# Create your views here.

def header(request):
    return render (request,'header.html')

def about(request):
    return render(request,'about.html')

def report(request):
    data = Report.objects.all()  
    context = {
        'data' : data
    }
    return render(request,'report.html',context)

def prediction(request):
    
     return render(request,'predictions.html')

def addreport(request):
    rep_form = ReportForm()
    if request.method == 'POST':
        city_name = request.POST['city_name']
        cur_con = request.POST['cur_con']
        temp = request.POST['temp']
        humidity = request.POST['humidity']
        wind = request.POST['wind']
        forecast = request.POST['forecast']
        print(city_name,cur_con,temp,humidity,wind,forecast)
        my_model = Report(city_name = city_name,cur_con = cur_con,temp = temp,humidity = humidity, wind = wind, forecast = forecast)
        my_model.save()
    data = Report.objects.all()    
    context = {
        'form' : rep_form,
        'data' : data
    }
    
    return render(request,'addreport.html',context)

def save_form(request):
    return HttpResponse("Details posted")