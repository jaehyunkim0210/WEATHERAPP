def recommend_outfit(temperature):
    #Recommend outfit based on temperature.
    if temperature > 20:
        return "T-shirt and shorts"
    elif temperature > 10:
        return "Long pants and a sweater"
    else:
        return "Winter coat and warm trousers"