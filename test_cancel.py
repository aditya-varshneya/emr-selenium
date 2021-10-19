import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

# Parameters
username = 8860879079
password = "Pass@12345"
name = "Test Automation"
age = 33
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"


# code elements
@pytest.mark.flaky(rerun=1)
def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_login():
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    driver.save_screenshot("./screenshots/test_cancel/login.png")
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_doc_reg():
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 30, 2)
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
        "/html/body/div/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div[1]/div/label/input").click()
    driver.find_element_by_id("email").send_keys(email)
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    driver.save_screenshot("./screenshots/test_cancel/appt.png")
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_cancellation():
    booked = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")
    booked.click()
    driver.save_screenshot("./screenshots/test_cancel/cancel.png")
    time.sleep(3)
    appointment_button = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[1]")
    appointment_button.click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/button[2]").click()
    time.sleep(2)
    driver.find_element_by_name("cancelRemarks").send_keys("Need to cancel")
    driver.save_screenshot("./screenshots/test_cancel/cancel1.png")
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/section/div[2]/div/button").click()
    time.sleep(7)
    wait = WebDriverWait(driver, 10, 2)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span[2]/button"))).click()
    driver.save_screenshot("./screenshots/test_cancel/cancel2.png")
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_refund():
    driver.find_element_by_xpath("//*[@id='orders-dropdown']").click()
    time.sleep(5)
    driver.save_screenshot("./screenshots/test_cancel/refund.png")
    try:
        driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[6]/div/a[1]").click()
        time.sleep(5)

        edit_sts = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div[2]/"
                                                "div[2]/div/div[1]/table/tbody/tr/td[8]/button")
        if edit_sts.is_displayed():
            edit_sts.click()

        else:
            print("Appointment is a follow-up")

        change_to = driver.find_element_by_name("name")
        chang = Select(change_to)
        chang.select_by_value("ready")
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[3]/button").click()
        time.sleep(7)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/p/span/button").click()
        driver.save_screenshot("./screenshots/test_cancel/refund1.png")
        time.sleep(3)
        driver.back()
        time.sleep(3)
    except:
        print("Appointment is a follow-up")
        driver.close()
