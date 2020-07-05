from _ctypes import pointer
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import date
from selenium.webdriver import ChromeOptions
import logging
import pytest

# Parameters
username = 8860879079
password = "Pass@12345"
name = "Testing Automate"
age = 32
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"


# code elements

def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe",chrome_options=chrome_options)
    driver.get(ip_url)
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
    driver.find_element_by_id("settings-trigger").click()
    time.sleep(3)
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
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div/form/div["
                                 "12]/div/div/div/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[2]/div").click()
    driver.back()
    time.sleep(5)


def test_verify_presc_button():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr/td[7]/button[2]").click()

    time.sleep(7)


def test_verify_patient_upload():
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[5]/div").click()
    time.sleep(3)
    try:
        card_title = driver.find_element_by_xpath("//*[@id='patient']/div/div/div/div[2]/div[2]/div/div[1]/h4")
        if card_title.is_displayed():
            assert True
        else:
            assert ("No Patient uploads")
    except:
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[6]/a/i").click()
    time.sleep(7)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[6]/a/i").click()
    time.sleep(5)
    driver.back()
    time.sleep(6)


def test_verify_followup():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()
    var_2 = driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[5]/label").text
    if var_2 == "Done":
        apt = driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[1]")
        apt.click()
    else:
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[2]/td[7]/button[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div/button[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div/div/div/div[2]/div/div/div[2]/section/div[2]/div/div/div[2]/div/div[1]/div/button[1]").click() #time slot
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/section/div[5]/div/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span[2]/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div[1]/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.close()

