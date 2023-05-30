from django.shortcuts import render
import requests


def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?lat=53.893009&lon=lon=27.567444&appid=20fd5c34764021202072320d2d18ae58"

    city = 'Minsk'

    res = requests.get(url.format(city))

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    context = {'info': city_info}
    return render(request, 'weatherone/index.html',     context)
