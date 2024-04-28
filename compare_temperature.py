def compare_temperature(today_temp, yesterday_temp):
    #Compare today's temperature with yesterday's temperature. 
    #So that the user have sense of the weather not just by number.
    if today_temp > yesterday_temp:
        return "hotter"
    elif today_temp < yesterday_temp:
        return "colder"
    else:
        return "similar"