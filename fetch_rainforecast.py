import requests
def fetch_rainforecast(api_key, city):
    #Fetch the rainforecast data from OpenWeatherMap API.(same method as fetch_todayweather function above.)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    rain_mm = data.get('rain', {}).get('1h', 0)
    return rain_mm