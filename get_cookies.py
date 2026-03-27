import pickle
import time
from selenium import webdriver


service = "/home/lorenzo/Progetti/academic-portal-monitor/chromedriver-linux64/chromedriver"

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome-stable"

driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path=service), options=options)
driver.get("https://webeep.polimi.it/my/")

input("Log in to the academic portal and press Enter to continue...")

with open("cookies.pkl", "wb") as file:
    pickle.dump(driver.get_cookies(), file)

time.sleep(2)  # Wait for a moment to ensure cookies are saved properly
print("Cookies saved to cookies.pkl")
driver.quit()