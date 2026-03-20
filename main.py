from selenium import webdriver 
import time 
service = "/home/lorenzo/Progetti/academic-portal-monitor/chromedriver-linux64/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome-stable"

driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path=service), options=options)
driver.get("https://webeep.polimi.it/login/index.php")
time.sleep(5)
print(driver.title)
driver.quit()
