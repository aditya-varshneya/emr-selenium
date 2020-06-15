from _ctypes import pointer
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from selenium.webdriver import ChromeOptions
import logging
import pytest


# Parameters
username = "8851217366"
password = "Thb@12345"
name = "Test Automation"
age = 33
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"


# code elements

def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=chrome_options)
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
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(age)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div/form/div["
                                 "12]/div/div/div/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(5)


def test_refund():
    driver.find_element_by_xpath("/html/body/div/div/div/nav/div[2]/ul[1]/li[5]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[5]/div/a[1]").click()

    time.sleep(5)
    try:
        edit_sts = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div[2]/"
                                                "div[2]/div/div[1]/table/tbody/tr/td[8]/button")
        if edit_sts.is_displayed():
            edit_sts.click()

        else:
            print("Appointment is a follow-up")

    except None:
        pass

    change_to = driver.find_element_by_name("name")
    chang = Select(change_to)
    chang.select_by_value("ready")
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[3]/button").click()
    time.sleep(5)
    driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/div/div/div/div/div/div[3]/div[2]/p/span/button").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.close()
