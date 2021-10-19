import time
import random
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Parameters
username = 8860879079
username_1 = 8287529291
password = "Pass@12345"
pass_1 = "Pass@1234"
name = "Automation test"
age = [32, 33, 34, 35]
phone = [9582944108, 8860879079]
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"


# code elements
@pytest.mark.flaky(rerun=1)
def test_setup_login():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()
    driver.delete_all_cookies()
    time.sleep(3)
    # Application login
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    driver.save_screenshot("./screenshots/test_setup/login.png")
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_patient_registration():
    # patient registration
    time.sleep(5)
    wait = WebDriverWait(driver, 30,2)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(4)
    driver.find_element_by_id("optionsRadios1").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(3)
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(random.choice(age))
    driver.find_element_by_id("phone").send_keys(random.choice(phone))
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div[1]/div/label/input").click()

    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    driver.save_screenshot("./screenshots/test_setup/appt.png")
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    time.sleep(10)
    driver.close()

@pytest.mark.flaky(rerun=1)
def test_setup_login_2():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()
    time.sleep(2)
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username_1)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(pass_1)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    driver.save_screenshot("./screenshots/test_setup/login2.png")
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_patient_registration_2():
    # patient registration
    wait = WebDriverWait(driver, 40,2)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(4)
    driver.find_element_by_id("optionsRadios1").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(3)
    doc_name = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/div/div/"
                                            "div/div/div/form/div[1]/div[2]/div/div/div")
    doc_name.click()
    search= driver.find_element_by_xpath("//*[@id='react-select-2-input']")
    time.sleep(1)
    search.send_keys("Doc")
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    invoice_fees = driver.find_element_by_name("invoice_amount")
    drp = Select(invoice_fees)
    drp.select_by_value("1")
    time.sleep(1)
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(random.choice(age))
    driver.find_element_by_id("phone").send_keys(random.choice(phone))
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div[1]/div/label/input").click()

    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    driver.save_screenshot("./screenshots/test_setup/appt2.png")
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    time.sleep(10)
    driver.save_screenshot("./screenshots/test_setup/apptlist.png")
    driver.close()
