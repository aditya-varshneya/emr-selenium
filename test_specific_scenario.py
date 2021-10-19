import datetime
import random
import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Parameters
username = 1234567895
password = "Pass@1234"
name = "Testing Automate"
age = [6, 7, 8]
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
radio = ["online", "offline"]

length = int(10)


def discount(length):
    num = "1234567890"
    pass_q = ''
    for c in range(length):
        pass_q += random.choice(num)
    return pass_q


mobile = (discount(length)).split(",") * 5


# code elements

@pytest.mark.flaky(rerun=1)
def test_setup_specific():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.delete_all_cookies()
    driver.maximize_window()


@pytest.mark.flaky(rerun=1)
##("Validation of login credentials")
def test_login_staff():
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    driver.save_screenshot("./screenshots/test_specific_scenario/login_zydus.png")
    time.sleep(6)


@pytest.mark.flaky(rerun=1)
##("Patient Registration with zydus specific case")
def test_patient_reg():
    wait = WebDriverWait(driver, 40, 2)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(5)
    doc_name = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/div/div/"
                                            "div/div/div/form/div[1]/div[2]/div/div/div")
    doc_name.click()
    time.sleep(2)
    search = driver.find_element_by_xpath("//*[@id='react-select-2-input']")
    time.sleep(1)
    search.send_keys("zydus")
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(int(random.choice(age)))
    driver.find_element_by_xpath("//*[@id='gender']").click()
    driver.find_element_by_id("guardian_name").send_keys("Testing")
    driver.find_element_by_id("guardian_phone").send_keys("9582944108")
    time.sleep(2)
    driver.save_screenshot("./screenshots/appt_zydus.png")
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/"
                                 "div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div["
                                                           "2]/p/span/button"))).click()
    driver.save_screenshot("./screenshots/test_specific_scenario/apptbooked_zydus.png")
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency()
##("Validation of search functionality from patient registration form")
def test_search_patient():
    WebDriverWait(driver, 40, 2).until(EC.visibility_of_element_located((By.ID, "settings-trigger"))).click()
    time.sleep(5)
    WebDriverWait(driver, 40, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div/div/div/"
                                                    "div/div/div/form/div[1]/div[2]/div/div/div"))).click()
    search = driver.find_element_by_xpath("//*[@id='react-select-3-input']")
    time.sleep(1)
    search.send_keys("zydus")
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_id("phone").send_keys("9876543456")
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/"
                                 "div/div/form/div[7]/div[1]/div/div[2]/div/div/button").click()
    time.sleep(20)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/table/tbody/tr/td[3]/button").click()
    driver.save_screenshot("./screenshots/test_specific_scenario/search_zydus.png")
    time.sleep(5)
    try:
        guardian_name = driver.find_element_by_id("guardian_name")
        assert guardian_name.is_displayed(), "Guardian name not displayed"
        guardian_name.clear()
        time.sleep(2)
        guardian_name.send_keys("Test Guard")
        time.sleep(2)
        guardian_phone = driver.find_element_by_id("guardian_phone")
        assert guardian_phone.is_displayed(), "Guardian phone not displayed"
        guardian_phone.clear()
        time.sleep(2)
        guardian_phone.send_keys(random.choice(mobile))
        time.sleep(2)
    except NoSuchElementException:
        print("Guardian name & Phone not available")
    driver.save_screenshot("./screenshots/test_specific_scenario/searchappt.png")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/"
                                 "div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    try:
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/p/span[2]/button').click()
        time.sleep(5)
        WebDriverWait(driver, 30, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div["
                                                        "2]/p/span/button"))).click()
    except:
        WebDriverWait(driver, 30, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div["
                                                        "2]/p/span/button"))).click()

    time.sleep(7)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_search_patient"])
def test_verify_status():
    global booked
    booked = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")
    booked.click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[3]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[4]/div/input").send_keys(
        "test")
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_search_patient"])
def test_verify_info():
    info = driver.find_element_by_xpath("//*[@id='patient-info']/i")
    assert info.is_displayed(), False
    info.click()
    driver.save_screenshot("./screenshots/test_specific_scenario/info_zydus.png")
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_search_patient"])
def test_verify_age():
    age = driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a[1]/p/strong")
    assert age.is_displayed(), True
    driver.save_screenshot("./screenshots/test_specific_scenario/age_zydus.png")
    time.sleep(2)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_search_patient"])
def test_verify_hid():
    hid = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a[5]/p/strong")
    if hid.is_displayed():
        assert "True"
    else:
        print("HID not available")
    driver.save_screenshot("./screenshots/test_specific_scenario/HID_zydus.png")
    time.sleep(2)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_search_patient"])
##("Verifying guardian name")
def test_guardian_name():
    guardian_name = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/"
                                                 "div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a[3]/p/strong")
    if guardian_name.is_displayed():
        assert "True"
    else:
        print("Guardian name not available")
    driver.save_screenshot("./screenshots/test_specific_scenario/guardianame_zydus.png")
    time.sleep(3)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_search_patient"])
##("Verifying Guardian phone number")
def test_guardian_phone():
    guardian_phone = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/"
                                                  "div/div[2]/table/tbody/tr[1]/td[7]/div/a[4]/p/strong")
    assert guardian_phone.is_displayed(), "Guardian phone not available"
    driver.save_screenshot("./screenshots/test_specific_scenario/guardianphone_zydus.png")


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_search_patient"])
##("Verfying patient payment type")
def test_payment_type():
    payment_type = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/"
                                                "div/div[2]/table/tbody/tr[1]/td[7]/div/a[8]/p/span").text

    try:
        assert "New" in payment_type, "Payment type wrong"
    except:
        if payment_type == "Followup":
            print("Appointment is follow-up")
        else:
            pass
    driver.save_screenshot("./screenshots/test_specific_scenario/paymenttype_zydus.png")
    time.sleep(2)

    driver.close()
