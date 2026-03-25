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
#time.sleep(20)

try:
    cookie_accept = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div[2]"))
    )
    cookie_accept.click()
except:
    print("Cookie banner not found")

time.sleep(5)
try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
finally:
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

try:
    full_screen = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='movie_player']/div[24]/div[2]/div[2]/div[2]/button[3]"))
    )
finally:
        full_screen.click()


input("Press Enter to exit...")
driver.quit()
