from django.db import models

# Create your models here.




class Report(models.Model):
     city_name = models.CharField(max_length=50,null=True)
     cur_con = models.CharField(max_length=50,null=True)
     temp = models.IntegerField(null=True)
     humidity = models.IntegerField(null=True)
     wind = models.CharField(max_length=50,null=True)
     forecast = models.CharField(max_length=50,null=True)