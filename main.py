from http import cookies
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
service = "/home/lorenzo/Progetti/academic-portal-monitor/chromedriver-linux64/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome-stable"

driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path=service), options=options)
driver.get("https://webeep.polimi.it/my/")
cookies = driver.get_cookies()
time.sleep(60)    # wait for the user to log in

try:
    main_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "region-main-box"))
    )
finally:
    print(cookies)

#search = driver.find_element(By.ID, "searchinput-69c42e5adc5dc69c42e5acfc6e3")
#search.send_keys("Fisica")

print(driver.title)
driver.quit()
