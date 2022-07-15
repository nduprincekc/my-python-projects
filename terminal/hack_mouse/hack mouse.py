import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(15)
    for i in range(0,100):
        pyautogui.moveTo(2, i * 5)
