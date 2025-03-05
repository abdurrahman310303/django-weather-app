import requests
from django.shortcuts import render

API_KEY = "752ffeec4c3e378bbec5d51175eaee27"  # Replace with your OpenWeather API key

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        return data
    else:
        return {"error": "City not found"}

def weather_view(request):
    weather_data = None
    default_cities = ["Lahore", "Islamabad", "Peshawar", "Karachi"]
    city_weather_data = {city: get_weather_data(city) for city in default_cities}

    if request.method == "POST":
        city = request.POST.get("city")
        weather_data = get_weather_data(city)

    return render(request, "weather/weather.html", {
        "weather_data": weather_data,
        "city_weather_data": city_weather_data
    })
