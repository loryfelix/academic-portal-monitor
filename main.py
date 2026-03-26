import pickle
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

with open("cookies.pkl", "rb") as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.refresh()

try:
    main_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "region-main-box"))
    )
finally:
    print("Main page loaded")

# Il corso in questione è Fisica
try:    
    course = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="yui_3_18_1_1_1774533907511_18"]/text()'))
    )
finally:
    course.click()  

# La sezione in questione è Materiali del corso
try:    
    materials = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#section-2 > div.course-section-header.d-flex.flex-wrap.align-items-center > div.section_goto.bulk-hidden.ms-auto > a > span.dir-rtl-hide > i'))
    )
finally:    
    materials.click() 

# Il folder in questione sono le Esercitazioni
try: 
    folder = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="module-423286"]/div/div[2]/div[1]/div/div/div/div/a/span'))
    )
finally:    
    folder.click()  

lecture = driver.find_element(By.ID, "ÿgtvc1")
if len(lecture) > 6:
    print("Nuova esercitazione disponibile!")
else:
    print("Nessuna nuova esercitazione disponibile.")
    
print(driver.title)
driver.quit()
