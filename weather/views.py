from django.shortcuts import render, HttpResponse
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8518bf0a99e1ff04f2838a9405f00cbd').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "desc": (json_data['weather'][0]['description']),
            "longitude": str(json_data['coord']['lon']),
            "latitude": str(json_data['coord']['lat']),
            "temp": str(round(json_data['main']['temp']-273.15,2)) + ' °C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "visibility": str(int(json_data['visibility']/1000)),
            "windspeed": str(json_data['wind']['speed']),        
        }
    else:
        city = ''
        data = {}    
    return render(request, 'index.html', {'city': city, 'data': data})