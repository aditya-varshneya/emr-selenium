
from _ctypes import pointer
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ChromeOptions
import logging
import pytest



# Parameters
username = 8860879079
password = "Pass@12345"
name = "Test Automation"
age = 33
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"

# code elements
def test_login():
        global driver
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 1}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=chrome_options)
        driver.get(ip_url)
        driver.maximize_window()

        username_textbox = driver.find_element_by_id("exampleInputUsername")
        username_textbox.send_keys(username)
        password_textbox = driver.find_element_by_id("exampleInputUserpassword")
        password_textbox.send_keys(password)
        login_but = driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
        login_but.click()
        time.sleep(7)


def test_video():
        driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[3]").click()
        time.sleep(5)
        try:
           var_1 = driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr/td[7]/button[4]")
           if var_1.is_displayed():
                   var_1.click()
           else:
             print ( " No appointment to start video, Please add appointment ")
        except None:
                pass
        time.sleep(15)
        driver.find_element_by_xpath("//*[@id='root']/div/div/div/section/div[2]/div/div[2]/div/button[4]/i").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='#']/div/input").send_keys("C:/Users/Lenovo/Desktop/Python/file.png")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[3]/button").click()
        time.sleep(7)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button/span[1]").click()
        time.sleep(5)
        driver.back()
        time.sleep(5)
        driver.close()
