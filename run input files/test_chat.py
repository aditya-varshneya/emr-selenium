import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import requests
import time
import webbrowser
import datetime

patient_url = 'https://emrapi.hlthclub.in/patient'
appointment_url = 'https://emrapi.hlthclub.in/appointment'
# payment_url = 'https://clinyticsapi.hlthclub.in/t-payments'
user_url = 'https://emrapi.hlthclub.in/user'
doctor_id = '4e30fbe8-3131-4caa-b374-2e8eff54ccc0'
account_id_1 = 'new_demo_account'
appointment_date = str(datetime.date.today())
appointment_slot = str(datetime.datetime.today().strftime("%I:%M %p"))


@pytest.mark.flaky(rerun=1)
def test_link_generator():
    # test_create_patient():
    api_create_patient = "{}/onlinepatient".format(patient_url)
    body_get_account = {
        "name": "Aditya Kumar",
        "age": {
            "no_of_years": "32",
            "no_of_months": "",
            "no_of_days": 0
        },
        "gender": "male",
        "email": "aditya.varshneya@gmail.com",
        "phone": "9582944108",
        "country_code": "+91",
        "symptoms": "Fever, Chills",
        "guardian_name": "",
        "guardian_phone": "",
        "complaints": "",
        "speciality": "",
        "account_id": "new_demo_account",
        "account_type": "Clinic",
        "device_id": "e2071a9a745ade7d5a0a15239fd9d428"
    }

    response_status_create_patient = requests.post(url=api_create_patient, json=body_get_account)
    json_create_patient = response_status_create_patient.json()
    token_1 = json_create_patient['token']
    patient_id = json_create_patient['id']

    # test_request_tele_consult
    api_get_tele_consult = '{}/onlinepatient/consult/{}'.format(patient_url, patient_id)
    body_get_tele_consult = {'Authorization': token_1}
    header = {
        "doctor_id": doctor_id,
        "symptoms": "Fever, Chills",
        "appointment_date": appointment_date,
        "appointment_slot": appointment_slot,
        "account_id": "new_demo_account",
        "slot_type": "evening",
        "account_type": "Clinic",
        "device_id": "e2071a9a745ade7d5a0a15239fd9d428"
    }
    requests.post(url=api_get_tele_consult, json=header, headers=body_get_tele_consult)

    time.sleep(10)
    global chat_link
    # test_get_payment_link
    api_get_payment_link = '{}/onlineappointment/get-payment-link/{}'.format(appointment_url, patient_id)
    header_get_payment_link = {'Authorization': token_1}
    body = {"doctor_id": doctor_id,
            "appointment_date": appointment_date,
            "appointment_slot": appointment_slot,
            "account_id": "new_demo_account"
            }
    response_status_payment_link = requests.post(url=api_get_payment_link, json=body, headers=header_get_payment_link)
    json = response_status_payment_link.json()
    chat_link = json['chat_link']
    print(response_status_payment_link)
    print(chat_link)



url_2 = "https://clinytics.hlthclub.in/doctor-login"
username = 8860879079
password = "Pass@12345"
name = "Test Automation"
age = 33
phone = 8860879079
email = "aditya.varshneya@gmail.com"
option_radio = ["/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/label/input",
                "/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/label/input"]

@pytest.mark.flaky(rerun=1)
def test_site():
    url_1 = chat_link
    global driver
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--use-fake-ui-for-media-stream")
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=options)
    driver.get(url_1)
    driver.maximize_window()
    time.sleep(2)
    options.add_argument("--use-fake-ui-for-media-stream")
    time.sleep(5)

@pytest.mark.flaky(rerun=1)
def test_allow_webcam():
    driver.find_element_by_xpath(random.choice(option_radio)).click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(3)
    try:
        elem = driver.find_element_by_xpath("//*[@id='allow-webcam']/div/div/div[2]/div/div/button")
        if elem.is_displayed():
            elem.click()
    except NoSuchElementException:
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/section/div/div[2]/div/div/div[2]/div/button").click()
        time.sleep(3)
    try:
        element_1 = driver.find_element_by_xpath("//*[@id='notificationmodal']/div/div/div[2]/div/div/div/button")
        if element_1.is_displayed():
            element_1.click()

    except NoSuchElementException:
        pass

@pytest.mark.flaky(rerun=1)
def test_chat():
    driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/section/div/div[3]/a").click()
    time.sleep(4)
    text_box = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/section/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/textarea")
    if text_box.is_displayed():
        text_box.send_keys("Hi Doctor,I am waiting for my consultation and uploaded history")
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/section/div/div[3]/div/div/div[2]/div/div/div/div[3]/div/button/span").click()
    while not text_box.is_enabled():
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, text_box)))
    time.sleep(7)
    driver.close()

@pytest.mark.flaky(rerun=1)
def test_site_1():
    global driver
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=options)
    driver.get(url_2)
    driver.maximize_window()
    time.sleep(5)
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_intiate_chat():
    try:
        driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[5]/div").click()
        time.sleep(5)
        reply = driver.find_elements_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/section/div/div/div/div/a["
                                              "1]/div[3]/button")
        for replies in reply:
            replies.is_displayed()
            replies.click()
        text = driver.find_elements_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/"
                                             "section/div/div/div/div/a[1]/div[4]/div/textarea")
        for texts in text:
            texts.is_displayed()
            texts.send_keys("I will join soon")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div/section/"
                                                               "div/div/div/div/a[1]/div[4]/button"))).click()


    except NoSuchElementException:
        print("No Chat History Available")

    time.sleep(7)
    driver.close()
