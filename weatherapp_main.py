import PySimpleGUI as sg
from today_weather import today_weather 
from yesterday_weather import fetch_yesterday_weather 
from raining import raining 
from fetch_rainforecast import fetch_rainforecast
from compare_temperature import compare_temperature
from recommend_outfit import recommend_outfit 


layout = [
    [sg.Text("Weather Information", font=('Helvetica', 16))],
    # [sg.Text("Location(City): "), sg.InputText(key = '-LOCATION-')],
    [sg.Text(size=(40, 1), key='-WEATHER-')],
    [sg.Text(size=(40, 1), key='-OUTFIT-')],
    [sg.Text(size=(40, 1),key = '-RAIN-')],
    [sg.Button("Refresh"), sg.Button("Exit")]
]


window = sg.Window("Weather App", layout)

while True:
    event, values = window.read()

    api_key = 'c5bcaa9e52187e78b61339a89aafdc3f'  
    city = values['-LOCATION-']

    today_temp,latitude,longitude = today_weather(api_key, city)
    yesterday_temp =fetch_yesterday_weather(api_key,latitude,longitude)
    comparison = compare_temperature(today_temp, yesterday_temp)
    outfit = recommend_outfit(today_temp)
    rainforecast = fetch_rainforecast(api_key,city)
    raining_dress = raining(rainforecast)
    
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Refresh':
        rain_text = f"Rain/Snow forecast for Today: {raining_dress}."
        weather_text = f"Today's temperature: {today_temp}°C, {comparison} than yesterday." 
        window['-RAIN-'].update(rain_text)
        window['-WEATHER-'].update(weather_text)
        window['-OUTFIT-'].update(f"Recommended outfit: {outfit}")
        
window.close()

