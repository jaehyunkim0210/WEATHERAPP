def raining(rain_mm):
    #Tell the user whether it is raining or not, so that they could dress accordingly.
    if rain_mm>0:
        return f"Raining {rain_mm}mm. Dress accordingly."
    else:
        return "No rain or snow expected"