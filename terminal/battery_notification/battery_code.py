import psutil
import plyer
from plyer import wifi



battery = psutil.sensors_battery()
percent = str(battery.percent)
r = battery.power_plugged
q = str(battery.secsleft )
print(help(psutil))


print('Your device has ' + percent + '% of battery remaining')
