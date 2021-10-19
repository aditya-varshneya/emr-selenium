import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Parameters
username = 8860879079
username_1 = 8287529291
password = "Pass@12345"
pass_1 = "Pass@1234"
name = "Web Testing"
age = 32
phone = 9582944108
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"


# code elements
@pytest.mark.flaky(rerun=1)
def test_setup_login():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()
    time.sleep(5)
    # Application login
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    driver.save_screenshot("./screenshots/test_cancel_scenario/login.png")
    login_but.click()
    time.sleep(10)

    # patient registration
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
    driver.save_screenshot("./screenshots/test_cancel_scenario/appt.png")
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    driver.save_screenshot("./screenshots/test_cancel_scenario/appt2.png")
    time.sleep(7)


@pytest.mark.flaky(rerun=1)
def test_cancel():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click()  # # booked tab
    # button element
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[4]/div/input").send_keys(
        name)
    driver.save_screenshot("./screenshots/test_cancel_scenario/cancel.png")
    try:
        test_name = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
                                                 "1]/div/div/div[2]/table/tbody/tr[1]/td[2]").text
        booked_status = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
                                                     "1]/div/div/div[2]/table/tbody/tr[1]/td[5]/label").text
        if test_name == name and booked_status == 'Booked':
            driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div["
                                         "2]/table/tbody/tr[1]/td[7]/button[1]").click()
        else:
            driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div["
                                         "2]/table/tbody/tr[2]/td[7]/button[1]").click()
    except NoSuchElementException:
        driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/"
                                     "div[1]/div/div/div[2]/table/tbody/tr[3]/td[7]/button[1]")
    time.sleep(4)
    driver.save_screenshot("./screenshots/test_cancel_scenario/cancel1.png")
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/button[2]").click()
    time.sleep(2)
    driver.find_element_by_name("cancelRemarks").send_keys("Need to cancel")
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/section/div[2]/div/button").click()
    time.sleep(7)
    wait = WebDriverWait(driver, 20, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span["
                                                           "2]/button"))).click()
    driver.save_screenshot("./screenshots/test_cancel_scenario/cancel3.png")
    time.sleep(7)
    driver.close()


@pytest.mark.flaky(rerun=1)
def test_patient_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()
    time.sleep(5)
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username_1)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(pass_1)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    driver.save_screenshot("./screenshots/test_cancel_scenario/login2.png")
    time.sleep(7)


@pytest.mark.flaky(rerun=1)
def test_patient_pending_reg():
    # patient registration
    global driver
    driver.delete_all_cookies()
    time.sleep(5)
    wait = WebDriverWait(driver, 40, 2)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(4)
    driver.find_element_by_id("optionsRadios1").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(3)
    doc_name = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/div/div/"
                                            "div/div/div/form/div[1]/div[2]/div/div/div")
    doc_name.click()
    search = driver.find_element_by_xpath("//*[@id='react-select-2-input']")
    time.sleep(1)
    search.send_keys("Doc")  # DoctorDemo
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    invoice_fees = driver.find_element_by_name("invoice_amount")
    drp = Select(invoice_fees)
    drp.select_by_value("1")
    time.sleep(1)
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(age)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div[1]/div/label/input").click()

    driver.find_element_by_id("email").send_keys(email)
    driver.save_screenshot("./screenshots/test_cancel_scenario/appt3.png")
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    time.sleep(10)
    driver.save_screenshot("./screenshots/test_cancel_scenario/appt2.png")
    driver.close()


'''
cancelled appointment check 
'''


@pytest.mark.flaky(rerun=1)
def test_check_status_cancel():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()
    time.sleep(5)
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(10)


@pytest.mark.flaky(rerun=1)
def test_verify_patient():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[4]/div/input").send_keys(
        name)
    new_status = len(driver.find_elements_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
                                                   "1]/div/div/div[2]/table/tbody/tr/td[5]/label"))
    driver.save_screenshot("./screenshots/test_cancel_scenario/patient.png")
    for status in range(1, new_status + 1):
        var = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
                                           "1]/div/div/div[2]/table/tbody/tr[" + str(status) + "]/td[5]/label").text
        # print(var)
        status = list(var.split(" , "))
        print(status, end='     ')
        if "Pending" in status:
            print("Status is correct")
        if "Cancelled" in status:
            print("Status is Correct")
        elif "Booked" in status:
            assert False
        time.sleep(3)
    driver.save_screenshot("./screenshots/test_cancel_scenario/patient1.png")
    driver.close()
