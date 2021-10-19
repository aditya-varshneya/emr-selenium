import random
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Parameters
username = 8287529291
password = "Pass@1234"
name = "Testing Automate"
age = 33
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
# radio = ["online"]
value_doc = ["cd4fdc4a-bfe3-456b-ac06-17a063acfedc", "4e30fbe8-3131-4caa-b374-2e8eff54ccc0",
             "d3e70041-302d-4cf5-9c5f-d62b1e712014",
             "9131cead-c520-4d6e-9049-babd3543f8c3", "253eedfe-f066-4242-9770-38cc8528516b",
             "1f37addc-66f2-4461-9bc1-47233cd006e0"]

value_name = ["Rohit Kumar", "Docotordemo", "Dr Kritika Tandon", "Nitin", "Dr Pushkin Negi", "Dr Adi"]


# code elements

@pytest.mark.flaky(rerun=1)
def test_setup_staff():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()


@pytest.mark.flaky(rerun=1)
def test_login_staff():
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    driver.save_screenshot("./screenshots/test_login_staff/login.png")
    time.sleep(6)


@pytest.mark.flaky(rerun=1)
def test_staff_reg():
    wait = WebDriverWait(driver, 10, 2)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(3)
    driver.find_element_by_name("online").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(5)
    doc_name = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/div/div/"
                                            "div/div/div/form/div[1]/div[2]/div/div/div")
    doc_name.click()
    search = driver.find_element_by_xpath("//*[@id='react-select-2-input']")
    time.sleep(1)
    search.send_keys("Doc")
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(age)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div/"
                                 "div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(7)
    driver.save_screenshot("./screenshots/test_login_staff/appt.png")
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div["
                                                           "2]/p/span/button"))).click()
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
def test_verify_status():
    global booked
    booked = WebDriverWait(driver, 30, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/"
                                                                                            "div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")))
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
##("Patient info on I icon validation")
def test_verify_info():
    driver.find_element_by_xpath("//*[@id='patient-info']/i").click()
    driver.save_screenshot("./screenshots/test_login_staff/info.png")
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
##("Patient age on I icon validation")
def test_verify_age():
    age = driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a["
        "1]/p/strong")
    assert age.is_displayed(), True
    driver.save_screenshot("./screenshots/test_login_staff/age.png")
    time.sleep(2)


##("Patient UHID in I icon validation")
@pytest.mark.flaky(rerun=1)
def test_verify_hid():
    hid = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/div/a[5]/p/strong")
    if hid.is_displayed():
        assert "True"
    else:
        print("HID not available")
    time.sleep(2)


@pytest.mark.flaky(rerun=1)
def test_appointment_button():  # verify appointment button
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click()
    time.sleep(3)
    button = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[8]/button[1]")
    driver.save_screenshot("./screenshots/test_login_staff/apptbutton.png")
    if button.is_displayed():
        print("Button is available")
    else:
        print("Appt Button not visible")
    time.sleep(2)
    text = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[8]/button[1]").text
    assert text == "Appt", True
    time.sleep(3)


@pytest.mark.flaky(rerun=1)
##("Verying no button other than links available on staff login")
def test_verify_cancelled():
    time.sleep(3)
    all = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/"
                                       "div/div/div[1]/div/div[1]/div/div[1]")
    all.click()
    time.sleep(2)
    cancelled_check = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]"
                                                   "/div/div/div[1]/div/div/div[1]/div/div[4]/div/input")
    cancelled_check.clear()
    cancelled_check.send_keys("cancel")
    driver.save_screenshot("./screenshots/test_login_staff/cancel.png")
    text = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr/td[8]/button").text
    assert "Links" == text
    time.sleep(2)
    cancelled_check.clear()
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[2]/div").click()
    driver.save_screenshot("./screenshots/test_login_staff/cancel2.png")
    driver.back()
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
##("Veryfying Transfer functionality")
def test_verify_transfer():
    global transfer
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[8]/button[1]").click()
    time.sleep(3)
    driver.save_screenshot("./screenshots/test_login_staff/transfer.png")
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/button[2]").click()
    time.sleep(3)
    shuffle_id = random.sample(value_doc, 3)
    shuffle_name = random.sample(value_name, 3)
    try:
        transfer = Select(driver.find_element_by_name("transfer_doctor_id"))
        transfer.select_by_value(random.choice(shuffle_id))
    except NoSuchElementException:
        transfer.select_by_visible_text(random.choice(shuffle_name))
    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[2]/div/"
                                 "div/div[2]/section/div[3]/div/div/div[2]/div/div[1]/div/button[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/section/div[5]/div/button").click()
    time.sleep(3)
    wait = WebDriverWait(driver, 20, 1)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span[2]/button"))).click()
    time.sleep(10)
    driver.save_screenshot("./screenshots/test_login_staff/transfer2.png")
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    time.sleep(3)
    driver.save_screenshot("./screenshots/test_login_staff/transfer3.png")
    driver.back()
    time.sleep(7)


@pytest.mark.flaky(rerun=1)
##("Verfying video link available on links when status is booked")
def test_link_booked():
    wait = WebDriverWait(driver, 20, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[1]/"
                                                           "div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]"))).click()
    time.sleep(3)
    driver.save_screenshot("./screenshots/test_login_staff/booked.png")
    try:
        links = driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td["
            "8]/button[3]")
        if links.is_displayed():
            links.click()
    except NoSuchElementException:
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[2]/td["
            "8]/button[3]").click()
    time.sleep(2)
    video = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/div/h5").text
    assert video == "Video Room"
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/div").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button/span[1]").click()
    time.sleep(3)


@pytest.mark.flaky(rerun=1)
##("Verfying payment link available on links when status is pending")
def test_link_pending():
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/"
                                 "div/div/div[1]/div/div[1]/div/div[1]").click()
    time.sleep(3)
    input_box = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/"
                                             "div/div/div[1]/div/div/div[1]/div/div[4]/div/input")
    input_box.clear()
    input_box.send_keys("pending")
    time.sleep(3)
    driver.save_screenshot("./screenshots/test_login_staff/pending.png")
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/"
                                 "div[1]/div/div/div[2]/table/tbody/tr[1]/td[8]/button").click()
    payment = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/div/h5").text
    print(payment)
    if " Payment Link " in payment:
        assert "Correct link"
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/div/h5/i").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button/span[1]").click()
    time.sleep(1)
    input_box.clear()
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[2]/div").click()
    time.sleep(1)
    driver.back()
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
##("Verfying follow up case")
def test_verify_followup():
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()
    wait = WebDriverWait(driver, 10)
    var_2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[1]/"
                                                                   "div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[6]/label"))).text
    driver.save_screenshot("./screenshots/test_login_staff/followup.png")
    if var_2 == "Done":
        apt = driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td["
            "8]/button[1]")
        apt.click()
    else:
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[2]/td[8]/button[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/button[1]").click()
    time.sleep(5)
    driver.save_screenshot("./screenshots/test_login_staff/followup2.png")
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/section/div[2]/div/div/div[2]/div/div[1]/div/button[1]").click()  # time slot
    time.sleep(5)
    driver.find_element_by_name("nextAppointmentRemarks").send_keys("Need a follow up")
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/section/div[5]/div/button").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span[2]/button").click()
    time.sleep(7)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/"
                                                           "div[2]/div[2]/p/span/button"))).click()
    driver.save_screenshot("./screenshots/test_login_staff/followup3.png")
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.close()
