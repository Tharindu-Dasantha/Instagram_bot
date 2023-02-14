import pyautogui as pg
import time 

#time.sleep(3)
#print(pg.position())

# Cllickin on the github desktop icon
pg.leftClick(1051, 1058, 1, 2)

# Clicking on the commit massege
pg.leftClick(128, 792, 1, 2)
pg.write("commit")
time.sleep(1)

#Clicking on the commi button
pg.leftClick(189, 990, 1, 2)

#pg.leftClick(1051, 1058, 1, 2)