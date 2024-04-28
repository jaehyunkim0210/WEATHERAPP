import requests
from datetime import datetime, timedelta

def fetch_yesterday_weather(api_key, latitude, longitude):
    #Fetch yesterday's weather data using the OpenWeatherMap one call timemachine API.
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_timestamp = int(yesterday.timestamp())
    yesterday_url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={latitude}&lon={longitude}&dt={yesterday_timestamp}&appid={api_key}&units=metric"
    yesterday_response = requests.get(yesterday_url)
    yesterday_data = yesterday_response.json()
    yesterday_temp = yesterday_data['current']['temp']
    return yesterday_temp