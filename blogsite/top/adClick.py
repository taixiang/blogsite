import os
import time
import random

def click():
    click1 = "adb shell input tap 500 400"
    os.system(click1)

    s1 = random.uniform(2, 5)
    time.sleep(s1)

    click2 = "adb shell input tap 512 1200"
    os.system(click2)


click()