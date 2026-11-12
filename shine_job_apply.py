from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = ChromeService(executable_path=r"C:\Users\ASUS\OneDrive\Desktop\Eclipse\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    driver.get("https://www.shine.com")
    print("Opened Shine.com")
    driver.save_screenshot('00_shine_home.png')
    time.sleep(2)

    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Login']"))
    )
    login_btn.click()
    print("Clicked Login")
    driver.save_screenshot('01_login_popup.png')
    time.sleep(2)

    email = "abcdefgh"
    password = "**********"

    email_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[name='email']"))
    )
    email_field.clear()
    email_field.send_keys(email)
    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password'], input[name='password']")
    password_field.clear()
    password_field.send_keys(password)
    driver.save_screenshot('02_credentials_entered.png')

    submit_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'cls_base_1_pw_login_btn') and contains(text(),'Login')]")
        )
    )
    submit_btn.click()
    print("Clicked Login submit in popup!")
    time.sleep(4)
    driver.save_screenshot('03_login_clicked.png')

    driver.get("https://www.shine.com/job-search/software-tester-jobs-in-hyderabad-2-years")
    print("Navigated to job search page")
    driver.save_screenshot('04_job_search.png')
    time.sleep(3)

    job_cards = driver.find_elements(By.CSS_SELECTOR, "li[class*='jobCard']")
    if len(job_cards) < 2:
        print("ERROR: less than 2 jobs found, can't proceed.")
        driver.save_screenshot('05_few_jobs_error.png')
        driver.quit()
        exit()

    second_job = job_cards[1]
    print("Second Job Card Text:")
    print(second_job.text)
    lines = second_job.text.split('\n')
    job_title = lines[0] if len(lines) > 0 else "Unknown"
    company_name = lines[1] if len(lines) > 1 else "Unknown"
    print(f"Selected job: {job_title} at {company_name}")
    second_job.click()
    driver.save_screenshot('06_second_job_selected.png')

    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        print("Switched to job details tab.")
    time.sleep(2)

    # --- Robust Apply Button Click ---
    apply_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Apply')]"))
    )
    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", apply_btn)
    time.sleep(1)
    # Try regular click first
    try:
        apply_btn.click()
        print("Clicked Apply (normal click)")
    except Exception as e:
        print("Normal click failed, trying JavaScript click")
        # JavaScript click for covered/intercepted buttons
        driver.execute_script("arguments[0].click();", apply_btn)
        print("Clicked Apply (JavaScript force)")

    driver.save_screenshot('07_applied_clicked.png')
    time.sleep(2)

    applied = False
    try:
        status_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Applied') or contains(text(),'applied')]"))
        )
        print("Application status:", status_msg.text)
        driver.save_screenshot('08_applied_confirmation.png')
        applied = True
    except Exception as e:
        print("Could not auto-confirm 'Applied' status, check manually.")

    print("="*40)
    print("APPLICATION FINISHED")
    print("Current page title:", driver.title)
    print("Current page URL:", driver.current_url)
    print(f"Job applied: {job_title} ({company_name})")
    if applied:
        print("Status: Application VERIFIED")
    else:
        print("Status: Application NOT VERIFIED (check screenshot)")

finally:
    driver.quit()
