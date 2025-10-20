from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# --- Setup Chrome options (optional) ---
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # open browser maximized

# --- Initialize Chrome driver ---
service = Service(r"C:\Users\fayaz\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # replace with your chromedriver path
driver = webdriver.Chrome(service=service, options=chrome_options)

# --- Open Instagram login page ---
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)  # wait for page to load

# --- Enter username and password ---
username_input = driver.find_element(By.XPATH, "//input[@name='username']")
password_input = driver.find_element(By.XPATH, "//input[@name='password']")

username_input.send_keys("fayazkhan_14")  # replace with your username
password_input.send_keys('Cigna@2022')  # replace with your password
password_input.send_keys(Keys.RETURN)

# --- Wait for login to complete ---
time.sleep(20)

# --- Optional: Check login success ---
if "accounts/login" not in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")

# --- Close browser ---
driver.quit()