from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---- Replace with your details ----
NAUKRI_EMAIL = "username@email.com"
NAUKRI_PASSWORD = "password"
RESUME_PATH = r"path\to\resume.pdf"


# Setup driver
options = webdriver.ChromeOptions()
# Comment this line while debugging so you can see browser
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# Open login page
driver.get("https://www.naukri.com/nlogin/login")

try:
    # Wait for username field and type
    username = wait.until(EC.presence_of_element_located((By.ID, "usernameField")))
    username.clear()
    username.send_keys(NAUKRI_EMAIL)

    # Wait for password field and type
    password = wait.until(EC.presence_of_element_located((By.ID, "passwordField")))
    password.clear()
    password.send_keys(NAUKRI_PASSWORD)

    # Click login button
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_btn.click()

    # Pause a bit so you can see what happens
    time.sleep(5)

    driver.save_screenshot("after_login.png")
    print("✅ Attempted login, check after_login.png")

    # Step 2: Go to Profile page
    wait.until(EC.url_contains("naukri.com"))
    driver.get("https://www.naukri.com/mnjuser/profile")

    # Step 3: Upload Resume
    upload = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    upload.send_keys(RESUME_PATH)

    print("✅ Resume refreshed!")

    time.sleep(5)

except Exception as e:
    print(f"❌ Error: {e}")
    driver.save_screenshot("error.png")

finally:
    driver.quit()
