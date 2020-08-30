import time
import random
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url_1 = "https://clinytics.hlthclub.in/new_demo_account/waiting-area/7915996617557" # need to add fresh link
url_2 = "https://clinytics.hlthclub.in/doctor-login"
username = 8860879079
password = "Pass@12345"
name = "Test Automation"
age = 33
phone = 8860879079
email = "aditya.varshneya@gmail.com"
option_radio = ["/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/label/input",
                "/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/label/input"]


def test_site():
    global driver
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=options)
    driver.get(url_1)
    driver.maximize_window()
    time.sleep(5)


def test_allow_webcam():
    driver.find_element_by_xpath(random.choice(option_radio)).click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(3)
    try:
        elem = driver.find_element_by_xpath("//*[@id='allow-webcam']/div/div/div[2]/div/div/button")
        if elem.is_displayed():
            elem.click()
    except NoSuchElementException:
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/section/div/div[2]/div/div/div[2]/div/button").click()
        time.sleep(3)
    try:
        element_1 = driver.find_element_by_xpath("//*[@id='notificationmodal']/div/div/div[2]/div/div/div/button")
        if element_1.is_displayed():
            element_1.click()

    except NoSuchElementException:
        pass


def test_chat():
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/section/div/div[3]/a").click()
    time.sleep(4)
    text_box = driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/section/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/textarea")
    if text_box.is_displayed():
            text_box.send_keys("Hi Doctor,I am waiting for my consultation and uploaded history")
    time.sleep(3)
    driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div/div/section/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/button/span").click()
    while not text_box.is_enabled():
        wait = WebDriverWait(driver,10)
        wait.until(EC.visibility_of_element_located((By.XPATH,text_box)))
    time.sleep(7)


def test_site_1():
    global driver
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=options)
    driver.get(url_2)
    driver.maximize_window()
    time.sleep(5)
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(7)


def test_intiate_chat():
    try:
        driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[5]/div").click()
        time.sleep(5)
        reply = driver.find_elements_by_xpath("//*[@id='root']/div/div/div/div/div/section/div/div/div/div/a[1]/div[3]/button")
        for replies in reply:
            replies.is_displayed()
            replies.click()
        text =driver.find_elements_by_xpath("//*[@id='root']/div/div/div/div/div/"
                                         "section/div/div/div/div/a[1]/div[4]/div/textarea")
        for texts in text:
            texts.is_displayed()
            texts.send_keys("I will join soon")
        wait = WebDriverWait(driver,10)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='root']/div/div/div/"
                                                              "div/div/section/div/div/div/div/a/div[4]/button"))).click()
    except NoSuchElementException:
        print ("No Chat History Available")

    time.sleep(7)
    driver.close()
