import requests

def fetch_yesterday_weather(api_key, latitude, longitude,todaytime):
    # Fetch yesterday's weather data using the OpenWeatherMap One Call Timemachine API.
    # Used Unix time, making the yesterday_timestamp 86400 seconds away from current time. 
    
    yesterday_timestamp = todaytime -86400
    yesterday_url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={latitude}&lon={longitude}&dt={yesterday_timestamp}&appid={api_key}"
    yesterday_response = requests.get(yesterday_url)
    
    if yesterday_response.status_code == 200:  # Check if the request was successful
        yesterday_data = yesterday_response.json()
        if 'current' in yesterday_data:
            yesterday_temp = yesterday_data['current']['temp']
            return yesterday_temp
        else:
            return "Yesterday weather data not found."
    else:
        return f"Failed to fetch data: {yesterday_response.status_code}"
    
