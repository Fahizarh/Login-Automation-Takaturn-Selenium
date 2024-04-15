from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

user_email = 'faizahsalami1@gmail.com'
user_password = 'ThephysioQA@1'

# Open Takaturn Sign in Page
driver.get("https://takaturn.io/signin")

# Enter email address and password
driver.find_element(By.NAME, 'email').send_keys(user_email)
driver.find_element(By.NAME, 'password').send_keys(user_password)

# Click the login button
driver.find_element(By.ID, "login-btn").click()


# Wait for the login process to complete
time.sleep(5)

# Check if login is successful
if "dashboard" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser
driver.quit()
