from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Chrome setup ---
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("C:/Users/fayaz/Downloads/chromedriver-win64/chromedriver.exe")  # update path

driver = webdriver.Chrome(service=service, options=chrome_options)

# --- Open Google My Activity ---
driver.get("https://myactivity.google.com/myactivity?pli=1")
wait = WebDriverWait(driver, 20)

# --- Log in manually (wait for user to enter credentials if needed) ---
print("Please log in manually in the opened browser...")
time.sleep(20)  # give time to manually login

# --- Wait for search history element to appear ---
# Example: interacting with the first search history item
try:
    # Adjust XPath according to your actual element
    search_item_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz[5]/c-wiz/div/div[1]/c-wiz[11]/div/div/div[2]/div[1]'
    search_item = wait.until(EC.visibility_of_element_located((By.XPATH, search_item_xpath)))
    print(search_item.text)

    # Print text or click it
    print("First search history item:", search_item.text)
    # search_item.click()  # uncomment if you want to click it
except Exception as e:
    print("Error:", e)

# --- Close browser ---
driver.quit()
