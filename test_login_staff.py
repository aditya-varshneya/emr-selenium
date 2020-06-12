from _ctypes import pointer
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import Select
import logging
import pytest




# Parameters
username = "8287529291"
password = "Pass@1234"
name = "Test Automation"
age = 33
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
# code elements


def test_setup_staff():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()


def test_login_staff():
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(7)


def test_staff_reg():
    driver.find_element_by_id("settings-trigger").click()
    time.sleep(3)
    doc_name = driver.find_element_by_name("doctor_id")
    drp = Select(doc_name)
    drp.select_by_value("cd4fdc4a-bfe3-456b-ac06-17a063acfedc")  #("cd4fdc4a-bfe3-456b-ac06-17a063acfedc")
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(age)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div/form/div["
                                 "12]/div/div/div/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(5)


def test_verify_status():
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[3]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[3]/div/input").send_keys("Rohit")
    time.sleep(5)

def test_verify_info():
    driver.find_element_by_xpath("//*[@id='patient-info']/i").click()
    time.sleep(5)
    driver.close()



