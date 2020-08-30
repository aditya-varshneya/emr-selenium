import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

# Parameters
username = 8860879079
password = "Pass@12345"
name = "selenium test"
age = 32
phone = "9582944108"
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
ip_site = "https://clinytics.hlthclub.in/new_demo_account/consult-online"


# code elements

def test_setup_login():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()

    # Application login
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(7)


def test_patient_registration():
    # patient registration
    wait = WebDriverWait(driver, 10)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(4)
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
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(7)


def test_cancel():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")  # # booked tab
    # button element
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[3]/div/input").send_keys(name)
    try:
        test_name = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div["
                                                 "2]/table/tbody/tr/td[2]").text
        booked_status = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/"
                                                     "div/div/div[2]/table/tbody/tr/td[5]/label").text
        if test_name=='Selenium Test' and booked_status=='Booked':
            driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/"
                                         "div[2]/table/tbody/tr/td[7]/button[1]").click()
        else:
            driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/"
                                         "table/tbody/tr[2]/td[7]/button[1]").click()
    except NoSuchElementException:
        driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]"
                                     "/table/tbody/tr[3]/td[7]/button[1]")
    time.sleep(4)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/div/button[2]").click()
    time.sleep(2)
    driver.find_element_by_name("cancelRemarks").send_keys("Need to cancel")
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/section/div[2]/div/button").click()
    time.sleep(7)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[2]/p/span[2]/button"))).click()
    time.sleep(7)
    driver.close()



def test_patient_setup():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=chrome_options)
    driver.get(ip_site)
    driver.maximize_window()
    time.sleep(7)

    '''
    code for patient registration form 
    '''
    driver.find_element_by_name("name").send_keys(name)
    driver.find_element_by_name("age:no_of_years").send_keys(age)
    element = driver.find_element_by_name("gender")
    drp = Select(element)
    drp.select_by_value("male")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/section[1]/div/div/div/div/div[2]/form/div[1]/div[5]/div/div/div/div/input").send_keys(
        phone)
    time.sleep(3)
    driver.find_element_by_name("symptoms").send_keys("Second booking")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='root']/div/div/section[1]/div/div/div/div/div[2]/form/div[3]/button").click()
    time.sleep(7)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/section[1]/div/div/div/div/div[2]/div/div[2]/p/span/button").click()
    # registration button
    try:
        otp = driver.find_element_by_name("otp")
        if otp.is_displayed():
            assert True
    except NoSuchElementException:
        pass

    time.sleep(7)

    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div[2]/div[5]/div[1]/div[2]/div/div[2]/a").click()  # Book Appointment Button
    time.sleep(12)
    time_slot = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[2]/div/"
                                             "div[1]/div[2]/section/div[3]/div/div/div[2]/div/div[1]/div/button[1]")  # time slot selection
    if time_slot.is_displayed():
        time_slot.click()
    else:
        driver.find_element_by_xpath("//*[@id='timeslotmodal']/div/div[1]/div[2]/section/"
                                     "div[3]/div/div/div[1]/div/div/div/ul/li[9]/a/i").click()
    time.sleep(8)
    driver.find_element_by_xpath("//*[@id='timeslotmodal']/div/div[1]/div[3]/button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(10)
    driver.close()


'''
cancelled appointment check 
'''


def test_check_status_cancel():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()

    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(10)


def test_verify_patient():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[3]/div/input").send_keys(
        "Second booking")
    time.sleep(3)
