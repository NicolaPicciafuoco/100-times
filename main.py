
import time
import pyautogui as pg

print(" program in 5 second ")
time.sleep(15)

for i in range(100):
    pg.write(" ti amo un botto")
    time.sleep(0.5)
    pg.press("enter")


