from django import forms


class ReportForm(forms.Form):
    city_name = forms.CharField(required=False,label="city")
    cur_con = forms.CharField(label="Current Condition")
    temp = forms.IntegerField(label="Temperature")
    humidity = forms.IntegerField(label="Humidity")
    wind = forms.CharField(label="Wind Speed")
    forecast = forms.CharField(label="Forecast")