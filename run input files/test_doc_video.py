import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

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
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=chrome_options)
    driver.get(ip_url)
    time.sleep(2)
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    driver.maximize_window()
    time.sleep(2)
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(17)


def test_video():
    try:
        driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[3]").click()
        time.sleep(5)
        try:
            video_button = driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td["
                "7]/button[4]")
            video_text = video_button.text
            if video_text == "Video":
                video_button.click()
            else:
                video_button_2 =driver.find_element_by_xpath(
                    "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[2]/td["
                    "7]/button[4]")
                video_2 = video_button_2.text
                if video_2 == "Video":
                    video_button_2.click()
        except NoSuchElementException:
            driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[3]/td["
                "7]/button[4]").click()
            print("Video button not found as appointment is offline in first two records")

        time.sleep(15)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[1]/div/div/section/div[2]/div/div[2]/div/button[4]/i").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='#']/div/input").send_keys("C:/Users/Lenovo/Desktop/Python/file.png")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div[3]/button[2]").click()
        time.sleep(7)
        driver.execute_script("window.scrollBy(0,500)", "")
        try:
            wait = WebDriverWait(driver, 30,2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/p/span"))).click()
        except:
            pass
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div[3]/button[1]").click()

        time.sleep(10)
    except:
        try:
            driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[3]/td["
                "7]/button[4]").click()

        except:
            driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[4]/td["
                "7]/button[4]").click()
        time.sleep(15)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[1]/div/div/section/div[2]/div/div[2]/div/button[4]/i").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='#']/div/input").send_keys("C:/Users/Lenovo/Desktop/Python/file.png")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div[3]/button[2]").click()
        time.sleep(7)
        driver.execute_script("window.scrollBy(0,500)", "")
        try:
            wait = WebDriverWait(driver, 30,3)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/p/span"))).click()
        except:
            pass
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div[3]/button[1]").click()

        time.sleep(10)
    finally:
        driver.close()
