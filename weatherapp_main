import PySimpleGUI as sg
import today_weather
import yesterday_weather
import raining
import fetch_rainforecast
import compare_temperature
import raining
import recommend_outfit


api_key = 'c5bcaa9e52187e78b61339a89aafdc3f'  # Replace with your actual API key
city = 'Chestnut Hill'

layout = [
    [sg.Text("Weather Information", font=("Helvetica", 16))],
    [sg.Text(size=(40, 1), key='-WEATHER-')],
    [sg.Text(size=(40, 1), key='-OUTFIT-')],
    [sg.Text(size=(40, 1),key = '-RAIN-')],
    [sg.Button("Refresh"), sg.Button("Exit")]
]


window = sg.Window("Weather App", layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Refresh':
        
        today_temp,latitude,longitude = today_weather(api_key, city)
        yesterday_temp = yesterday_weather(api_key,latitude,longitude)
        
        comparison = compare_temperature(today_temp, yesterday_temp)
        outfit = recommend_outfit(today_temp)

        rainforecast = fetch_rainforecast(api_key,city)
        raining_dress = raining(rainforecast)
        
        rain_text = f"Rain/Snow forecast for Today: {raining_dress}"
        weather_text = f"Today's temperature: {today_temp}°C, {comparison} than yesterday."
        
        window['-RAIN-'].update(rain_text)
        window['-WEATHER-'].update(weather_text)
        window['-OUTFIT-'].update(f"Recommended outfit: {outfit}")
window.close()
