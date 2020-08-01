import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Parameters
username = 8860879079
password = "Pass@12345"
name = "Testing Automate"
age = 32
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
content = [10,20,30, 120, 80, 23, 23, 130, 22]
keys = ["Yes, from 2 years", "From 7 Years", "Mild Symptoms","Severity high" ]


# code elements

def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", chrome_options=chrome_options)
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

@pytest.mark.skip
def test_doc_reg():
    wait = WebDriverWait(driver, 10)
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
        "/html/body/div/div/div/div/div/div/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div[1]/div/label/input").click()
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[2]/div").click()
    driver.back()
    time.sleep(5)


def test_verify_presc_template():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr/td[7]/button[2]").click()
    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    add = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/a[1]/span")))
    add.click()
    time.sleep(5)
    checkboxes = driver.find_elements_by_xpath("//*[@id='value']")
    for checkbox in checkboxes:
        if checkbox.is_displayed():
            checkbox.send_keys(random.choice(content))
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='content']/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/button").click()
    time.sleep(5)


def test_verify_patient_upload():
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[5]/div").click()
    time.sleep(3)
    try:
        card_title = driver.find_element_by_xpath("//*[@id='patient']/div/div/div/div[2]/div[2]/div/div[1]/h4")
        if card_title.is_displayed():
            assert True
        else:
            assert ("No Patient uploads")
    except NoSuchElementException:
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[6]/a/i").click()
    time.sleep(7)
    # driver.find_element_by_xpath("/html/body/div/div/div/div/div[6]/a/i").click()
    # time.sleep(5)
    driver.back()
    time.sleep(5)


def test_verify_case_history():
    wait = WebDriverWait(driver, 10)
    status_booked = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div/div[1]/"
                                                                           "div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")))
    status_booked.click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr/td[7]/button[2]").click()
    time.sleep(5)
    try:
        case_history_link = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[1]/div/div[2]/p/a")
        if case_history_link.is_displayed():
            driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[4]/div").click() ## Case History
        else:
            print("Case history already written")
    except NoSuchElementException:
        pass
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[4]/div").click()
    time.sleep(3)
    drop_down = driver.find_element_by_xpath("//*[@id='heading-13']/a/h6")
    if drop_down.is_enabled():
        driver.find_element_by_xpath("//*[@id='heading-13']/a/h6").click()
        time.sleep(6)
        socio_var = driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div/div/div/div[1]/"
                                                 "div/div[2]/div[2]/div/div[2]/div/div[1]/select")
        drp = Select(socio_var)
        drp.select_by_value("Upper")
    else:
       driver.find_element_by_xpath("//*[@id='heading-13']/a/h6").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='collapse-13']/div/div[2]/div/div[2]/input").send_keys("Patient has smoking habit")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div/div/div/div[1]/div/"
                                 "div[2]/div[2]/div/div[3]/div/div[1]/div/div[1]/label/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div/div/div/div[1]/div/"
                                 "div[2]/div[2]/div/div[4]/div/div[1]/input").send_keys("3")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='collapse-13']/div/div[4]/div/div[2]/input").send_keys("2")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div/div/div/div[1]/div/"
                                 "div[2]/div[2]/div/div[5]/div/div[1]/input").send_keys("18")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='collapse-13']/div/div[5]/div/div[2]/input").send_keys("7")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div/div/div/div[1]/div/div[2]"
                                 "/div[2]/div/div[6]/div/div[1]/div/div[1]/label/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div/div/div/div[1]/div/div[2]/"
                                 "div[2]/div/div[7]/div/div[1]/div/div[1]/label/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='collapse-13']/div/div[7]/div/div[2]/input").send_keys("7")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div/div/div/div[1]/div/div[2]/div[1]/a/h6").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/div/div/div/div[1]/div/div[3]/div[1]/a/h6").click()

    time.sleep(2)
    comment = driver.find_elements_by_name("comment")
    for comm in comment:
        if comm.is_displayed():
            comm.send_keys(random.choice(keys))
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='casehistory']/div/div/div/div[2]/button").click() ## Submit Button
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='casehistory']/div[2]/div[2]/p/span/button").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)

def test_verify_case():
    wait = WebDriverWait(driver, 10)
    status_booked = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div/div[1]/"
                                                                           "div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")))
    status_booked.click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr/td[7]/button[2]").click()
    time.sleep(5)
    case_history = driver.find_element_by_xpath("//*[@id='accordion-5']/div[1]/div/div/div[2]")
    assert case_history.is_displayed(),True
    time.sleep(3)
    driver.back()
    time.sleep(5)


def test_verify_reschedule():
    wait = WebDriverWait(driver, 10)
    status_booked = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")))
    status_booked.click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[1]").click()
    time.sleep(4)
    reschedule = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/div/button[3]")
    reschedule.click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/section/div[2]/div/div/div[2]/div/div/div/button[1]").click()
    time.sleep(3)
    driver.find_element_by_name("rescheduleRemarks").send_keys("Doctor not available")
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div[2]/div/div/div[2]/section/div[5]/div/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span[2]/button").click()
    time.sleep(5)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(3)
    driver.back()
    time.sleep(5)

    driver.close()
