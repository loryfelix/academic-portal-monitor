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
driver.get("https://www.youtube.com/")
time.sleep(15)    # wait for the user to log in

search = driver.find_element(By.NAME, "search_query")
search.send_keys("lo-fi")

search.send_keys(Keys.RETURN)

print("Ricerca effettuata")

try:
    video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video-title"))
    )
finally:
    video.click()
    print("video cliccato")

print(driver.title)
driver.quit()
