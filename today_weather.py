import requests
def today_weather(api_key, city):
    # Fetch the weather data from OpenWeatherMap API. 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    today_temp = data['main']['temp']
    todaytime = data['dt']
    return today_temp, data['coord']['lat'], data['coord']['lon'],todaytime
