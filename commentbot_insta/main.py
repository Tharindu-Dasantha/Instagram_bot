import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as cm


def main():
    options = webdriver.ChromeOptions()
    
    mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19" 
    }

    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--log-level=3")

    bot = webdriver.Chrome(options = options, executable_path=cm().install())
    bot.set_window_size(500, 950)

    bot.get('https://instagram.com/')

    # Logging section
    time.sleep(6)
    bot.find_element("xpath", "//*[@id=\"mount_0_0_zT\]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div[2]/div[3]/button[1]/div").click()
    time.sleep(3)
    
    username_field = bot.find_element("xpath", "//*[@id=\"loginForm\"]/div[1]/div[3]/div/label/input" )
    username_field.send_keys("instabot7788@gmail.com")
    time.sleep(1)
        
    password_field = bot.find_element("xpath", "//*[@id=\"loginForm\"]/div[1]/div[4]/div/label/input" )
    password_field.send_keys("ABCDEFGH119")
    time.sleep(2)
    
    bot.find_element("xpath", "//*[@id=\"loginForm\"]/div[1]/div[6]").click()
    time.sleep(12)
    
    
main()