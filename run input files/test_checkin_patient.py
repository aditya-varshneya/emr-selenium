import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import requests
import time
import webbrowser
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

patient_url = 'https://emrapi.hlthclub.in/patient'
appointment_url = 'https://emrapi.hlthclub.in/appointment'
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


option_radio = ["/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/label/input",
                "/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/label/input"]

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['platform'] = "WINDOWS"
capabilities['version'] = 10
capabilities['args'] = "--use-fake-device-for-media-stream"
capabilities['browserName'] = 'chrome'



@pytest.mark.flaky(rerun=1)
def test_site_1():
    url_1 = chat_link
    global driver
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--use-fake-ui-for-media-stream")
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=options,desired_capabilities=capabilities)
    driver.get(url_1)
    driver.maximize_window()
    time.sleep(2)
    options.add_argument("--use-fake-ui-for-media-stream")
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_allow_webcam():
    driver.find_element_by_xpath(random.choice(option_radio)).click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(5)
    try:
        elem = driver.find_element_by_xpath("//*[@id='allow-webcam']/div/div/div[2]/div/div/button")
        if elem.is_displayed():
            elem.click()
        else:
            driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/section/div/div[2]/div/div/div[2]/div/button").click()
    except NoSuchElementException:
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/section/div/div[2]/div/div/div[2]/div/button").click()
        time.sleep(3)

@pytest.mark.flaky(rerun=1)
def test_verify_image():
    image = driver.find_element_by_xpath("//*[@id='root']/div/nav/div[1]/a[1]/img").is_displayed()
    if image == True:
        assert True
    else:
        assert "logo is not available"
    time.sleep(3)

@pytest.mark.flaky(rerun=1)
def test_upload():
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/section/div/div[2]/div/div/div[1]/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='#']/div/input").send_keys("C:/Users/Lenovo/Desktop/Python/file.png")
    driver.find_element_by_name("reportName").send_keys("Previous Prescription")
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/div[6]/button[1]").click()
    wait = WebDriverWait(driver,30,2)
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[3]/div[2]/p/span/button"))).click()
    time.sleep(5)

@pytest.mark.flaky(rerun=1)
def test_run_video():
    try:
        element_1 = driver.find_element_by_xpath("//*[@id='notificationmodal']/div/div/div[2]/div/div/div/button")
        if element_1.is_displayed():
            element_1.click()

    except NoSuchElementException:
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div/div/section/div/div[2]/div/div/div[2]/div/div/button").click()

    time.sleep(15)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/section/div[2]/div/div[2]/div/button[4]").click()
    time.sleep(7)

@pytest.mark.flaky(rerun=1)
def test_view_chat():
    chat = driver.find_element_by_id("menu-share")
    if chat.is_displayed():
        assert True, "Test Passed"
    else:
        assert "Chat Button not available"
    time.sleep(5)

@pytest.mark.flaky(rerun=1)
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
        print("Chat UI Not Activated due to doctor not replied")
        driver.find_element_by_xpath("//*[@id='menu-close']/i").click()

    driver.close()
