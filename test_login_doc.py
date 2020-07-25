import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# Parameters
username = 8860879079
password = "Pass@12345"
name = "Testing Automate"
age = 32
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
content = ["Fever",120,80,23,23,130,22]

# code elements

def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", chrome_options=chrome_options)
    driver.get(ip_url)
    driver.delete_all_cookies()
    driver.maximize_window()


def test_login():
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(7)


def test_doc_reg():
    wait = WebDriverWait(driver, 10)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(5)
    driver.find_element_by_id("optionsRadios1").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(3)
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(age)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div/div/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div[1]/div/label/input").click()
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[2]/div").click()
    driver.back()
    time.sleep(5)


def test_verify_presc_template():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr/td[7]/button[2]").click()
    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    add = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/a[1]/span")))
    add.click()
    time.sleep(5)
    checkboxes = driver.find_elements_by_xpath("//*[@id='value']")
    for checkbox in checkboxes:
        if checkbox.is_displayed():
            checkbox.send_keys(random.choice(content))
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='content']/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/button").click()
    time.sleep(5)


def test_verify_patient_upload():
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[5]/div").click()
    time.sleep(3)
    try:
        card_title = driver.find_element_by_xpath("//*[@id='patient']/div/div/div/div[2]/div[2]/div/div[1]/h4")
        if card_title.is_displayed():
            assert True
        else:
            assert ("No Patient uploads")
    except NoSuchElementException:
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[6]/a/i").click()
    time.sleep(7)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[6]/a/i").click()
    time.sleep(5)
    driver.back()
    time.sleep(5)

def test_verify_reschedule():
    wait = WebDriverWait(driver,10)
    status_booked= wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")))
    status_booked.click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[1]").click()
    time.sleep(4)
    reschedule = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/div/button[3]")
    reschedule.click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/section/div[2]/div/div/div[2]/div/div/div/button[1]").click()
    time.sleep(3)
    driver.find_element_by_name("rescheduleRemarks").send_keys("Doctor not available")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/section/div[5]/div/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span[2]/button").click()
    time.sleep(3)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(3)
    driver.back()
    time.sleep(5)
    driver.close()