import psutil

battery = psutil.sensors_battery()
percent = str(battery.percent)
r = battery.power_plugged
q = str(battery.secsleft )

print('Your device has ' + percent + '% of battery remaining')
