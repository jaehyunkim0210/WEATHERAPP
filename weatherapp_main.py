import PySimpleGUI as sg
from today_weather import today_weather 
from yesterday_weather import fetch_yesterday_weather 
from raining import raining 
from fetch_rainforecast import fetch_rainforecast
from compare_temperature import compare_temperature
from recommend_outfit import recommend_outfit 

layout = [
    [sg.Text("Weather Information", font=('Helvetica', 16), key = '-WEATHER-')],
    [sg.Text("Location(City): "), sg.InputText(key = '-LOCATION-')],
    [sg.Text('Recommended outfit for the day', key = "-OUTFIT-")],
    [sg.Button("Refresh"), sg.Button("Exit")]
]

window = sg.Window("Weather App", layout)
event, values = window.read()

api_key = 'c5bcaa9e52187e78b61339a89aafdc3f'  
city = values['-LOCATION-']

today_temp,latitude,longitude,todaytime = today_weather(api_key, city)
today_temp = float(today_temp)
latitude = float(latitude)
longitude = float(longitude)

yesterday_temp =fetch_yesterday_weather(api_key,latitude,longitude,todaytime)
yesterday_temp = float(yesterday_temp)
comparison = compare_temperature(today_temp, yesterday_temp)
outfit = recommend_outfit(today_temp)
rainforecast = fetch_rainforecast(api_key,city)
rainforecast = float(rainforecast)

raining_dress = raining(rainforecast)

while True:
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Refresh':
        weather_text = f"Today's temperature: {today_temp}°C, {comparison} than yesterday." 
        rain_text = f"Rain/Snow forecast for Today: {raining_dress}."
        window['-WEATHER-'].update(weather_text)
        window['-RAIN-'].update(rain_text)
        window['-OUTFIT-'].update(f"Recommended outfit: {outfit}")
window.close()

