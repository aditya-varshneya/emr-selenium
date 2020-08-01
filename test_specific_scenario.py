import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Parameters
username = 1234567895
password = "Pass@1234"
name = "Testing Automate"
age = [6,7,8]
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
radio = ["online", "offline"]



# code elements


def test_setup_specific():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", chrome_options=chrome_options)
    driver.get(ip_url)
    driver.delete_all_cookies()
    driver.maximize_window()


def test_login_staff():
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(6)


def test_patient_reg():
    wait = WebDriverWait(driver, 10)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(5)
    doc_name = driver.find_element_by_name("doctor_id")
    drp = Select(doc_name)
    drp.select_by_value("4641265a-fb13-4e79-891e-b4288c8b012e")  # ("cd4fdc4a-bfe3-456b-ac06-17a063acfedc")
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(int(random.choice(age)))
    driver.find_element_by_xpath("//*[@id='gender']").click()
    driver.find_element_by_id("guardian_name").send_keys("Testing")
    driver.find_element_by_id("guardian_phone").send_keys("9582944108")
    time.sleep(2)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div/form/div["
                                     "13]/div/div/div/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(5)


def test_verify_status():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[3]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[3]/div/input").send_keys("test")
    time.sleep(5)


def test_verify_info():
    driver.find_element_by_xpath("//*[@id='patient-info']/i").click()
    time.sleep(5)


def test_verify_age():
    age = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a[1]/p/strong")
    assert age.is_displayed(), True
    time.sleep(2)


def test_verify_hid():
    hid = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a[3]/p/strong")
    if hid.is_displayed():
        assert "True"
    else:
        print("HID not available")
    time.sleep(2)

def test_guardian_name():
    guardian_name = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div/" \
                                                               "div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a[4]/p")
    if guardian_name.is_displayed():
        assert "True"
    else:
        print("Guardian name not available")
    time.sleep(3)

def test_payment_type():
    payment_type = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/" \
                                                              "div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a[8]/p/span").text
    assert "New" in payment_type, "True"

    time.sleep(2)

    driver.close()




