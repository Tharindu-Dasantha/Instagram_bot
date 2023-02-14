import pyautogui as pg
import time

time.sleep(2) # remove this late this is only for marking the times 

# printing out the cordinates needed
# print(pg.position())

# clicking on the chrome button
pg.leftClick(1113, 1046, 1, 1)
# cicking on the chrome account
pg.leftClick(1298, 469, 1, 1)
# clicking on the search bar
pg.leftClick(351, 66, 1, 1)
# typing the address
pg.write("https://www.instagram.com/")
# pressing enter
pg.press("enter")