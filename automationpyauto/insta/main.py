import pyautogui as pg
import time

time.sleep(2) # remove this late this is only for marking the times 

# printing out the cordinates needed
#print(pg.position())

# taking inputs to log into the insta account
username = input("Username: ")
password = input("Password: ")

# clicking on the chrome button
pg.leftClick(1113, 1046, 1, 2)

# cicking on the chrome account
pg.leftClick(1298, 469, 1, 1)
time.sleep(1)

# clicking on the search bar
pg.leftClick(351, 66, 1, 2)

# typing the address
pg.write("https://www.instagram.com/")
pg.press("enter")
time.sleep(5)

# clicking on the username bar
pg.leftClick(1153, 338, 1, 2)
pg.write(username)

# clicking on the password bar
pg.leftClick(1122, 399, 1, 1)
pg.write(password)
time.sleep(1)

# clicking on the log in button
pg.leftClick(1148, 449, 1, 1)