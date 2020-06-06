from _ctypes import pointer
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date
from selenium.webdriver import ChromeOptions
import logging
import pytest

logging.basicConfig(filename="C://Users//Lenovo//Desktop//logfile.log", format='%(asctime)s: %(levelname)s: %('
                                                                               'message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

# Parameters
username = 8851217366
password = "Thb@12345"
name = "Nitin"
age = 33
phone = 8860879079
email = "aditya.varshneya@gmail.com"


# code elements

def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=chrome_options)
    driver.get("https://clinytics.hlthclub.in/doctor-login")
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
    time.sleep(40)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/"
                                  "tbody/tr[1]/td[7]/button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/a[2]/span").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='#']/div/input").send_keys("C:/Users/Lenovo/Desktop/Python/file.png")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div/div/div[2]/div[4]/div/button[1]").click()
    time.sleep(7)
    driver.back()
    time.sleep(7)

today = date.today()
def test_verify_followup():
        driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[3]/div[1]/div/div/div[2]/div[1]"
                                     "/div/div[1]/div/input").send_keys(today.strftime("%d-%m-%Y"))
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/div/input").send_keys("6:30 PM")
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/div/div[3]/div[1]/div/div/div[3]/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
        driver.back()
        time.sleep(5)
        driver.close()







