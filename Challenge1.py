def h24_converter(hour,minute,period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{minute:02d}"


print(h24_converter(6,22,"am"))
print(h24_converter(6,22,"pm"))
