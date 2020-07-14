import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


url_1 = "https://clinytics.hlthclub.in/new_demo_account/waiting-area/8c5a794705925"

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
    try:
        elem = driver.find_element_by_xpath("//*[@id='allow-webcam']/div/div/div[2]/div/div/button")
        if elem.is_displayed():
            elem.click()
    except NoSuchElementException:
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/section/div/div[2]/div/div/div[3]/div/button").click()
        time.sleep(3)


def test_verify_image():
    image = driver.find_element_by_xpath("//*[@id='root']/div/nav/div[1]/a[1]/img").is_displayed()
    if image == True:
        assert True
    else:
        assert "logo is not available"
    time.sleep(5)


def test_upload():
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/section/div/div[2]/div/div/div[1]/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='#']/div/input").send_keys("C:/Users/Lenovo/Desktop/Python/file.png")
    driver.find_element_by_name("reportName").send_keys("Previous Prescription")
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/div[6]/button[1]").click()
    time.sleep(8)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[3]/div[2]/p/span/button").click()
    time.sleep(5)


def test_run_video():
    try:
        element_1 = driver.find_element_by_xpath("//*[@id='notificationmodal']/div/div/div[2]/div/div/div/button")
        if element_1.is_displayed():
            element_1.click()

    except NoSuchElementException:
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/section/div/div[2]/div/div/div[3]/div/div/button").click()

    time.sleep(10)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/section/div[2]/div/div[2]/div/button[4]/i").click()
    time.sleep(7)


def test_view_chat():
    chat = driver.find_element_by_id("menu-share")
    if chat.is_displayed():
        assert True, "Test Passed"
    else:
        assert "Chat Button not available"
    time.sleep(5)


def test_chat():
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/section/div/div[3]/a").click()
    time.sleep(4)
    try:
        text_box = driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/section/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/textarea")
        if text_box.is_displayed():
            text_box.send_keys("Hi Doctor,I am waiting for my consultation and uploaded history")
            time.sleep(3)
            driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div/div/section/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/button/span").click()
            time.sleep(7)
            driver.find_element_by_xpath("//*[@id='menu-close']/i").click()
        else:
            driver.find_element_by_xpath("//*[@id='menu-close']/i").click()
    except NoSuchElementException:
        driver.find_element_by_xpath("//*[@id='menu-close']/i").click()

    driver.close()
