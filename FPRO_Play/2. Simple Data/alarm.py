def alarm(hour, minutes):
    minutes += 51
    hour = (hour + 6 + (minutes // 60)) % 24
    minutes = minutes % 60
    return str(hour).zfill(2) + ":" + str(minutes).zfill(2)
