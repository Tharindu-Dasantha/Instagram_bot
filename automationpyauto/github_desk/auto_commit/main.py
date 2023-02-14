import pyautogui as pg
import time 

time.sleep(3)
print(pg.position())

# Cllickin on the github desktop icon
pg.leftClick(1051, 1058, 1, 2)

# Clicking on the commit massege
time.sleep(1)
pg.leftClick(193, 798, 1, 2)
pg.write("commit")
time.sleep(1)

# Clicking on the commi button
pg.leftClick(174, 990, 1, 2)
time.sleep(1)

# Clicking on push origin
pg.leftClick(1416, 359, 1, 2)