from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element("xpath", "//input[@name=\"username\"]")\
            .send_keys(username)   
        self.driver.find_element("xpath", "//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element("xpath", '//button[@type="submit"]')\
            .click()
        sleep(4)    
        


# Getting the username and password form the user
username = input("Username: ")
password = input("Password: ")


InstaBot(username, password)