from django.contrib import admin

# Register your models here.

from myapp.models import Report

class Reportdetails(admin.ModelAdmin):
    list_display = ['city_name','cur_con','temp','humidity','wind','forecast']



admin.site.register(Report,Reportdetails)