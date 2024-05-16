#!/usr/bin/env python3

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Replace these variables with your Greythr credentials
username = "1450"
password = "2014Gu$9@college"

# Path to your WebDriver. Make sure you provide the correct path.
webdriver_path = "/home/guruprasad/Downloads/msedgedriver"

# Initialize Edge WebDriver service and options
service = Service(webdriver_path)
options = Options()
options.use_chromium = True

# Initialize Edge WebDriver
driver = webdriver.Edge(service=service, options=options)

# Open Greythr login page
driver.get("https://wisdomleaf.greythr.com/uas/portal/auth/")

# Find username and password fields and input credentials
username_field = WebDriverWait(driver, 300).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username_field.send_keys(username)

password_field = WebDriverWait(driver, 300).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for login
WebDriverWait(driver, 300).until(
    EC.url_contains("dashboard")  # Wait until the URL contains "dashboard"
)

print("Logged in successfully. Performing tasks...")

# Do your work here after login
# You can add logic to check the current time and determine when to logout
# For demonstration purposes, we'll wait for 10 seconds and then logout
time.sleep(300)

# Log out
logout_button = WebDriverWait(driver, 300).until(
    EC.presence_of_element_located((By.ID, "logoutButton"))
)
logout_button.click()

print("Logged out successfully.")

# Close the browser
driver.quit()
