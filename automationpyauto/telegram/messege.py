import pyautogui as pg
import time

time.sleep(1)

#print(pg.position())
pg.leftClick(651, 29, 1, 2)
time.sleep(1)
pg.typewrite("web.telegram.org/z/")
time.sleep(1)
pg.press("enter")
