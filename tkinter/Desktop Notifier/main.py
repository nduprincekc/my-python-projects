from plyer import notification
import time
while True:
    notification.notify(title='DRINK WATER',
                        message="Drink water to surprise your liver",
                        app_icon='glass.ico',
                        timeout=2)

    time.sleep(30*60)