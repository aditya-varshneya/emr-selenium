import datetime
import random
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

# Parameters
username = 8860879079
password = "Pass@12345"
name = "Testing Automate"
age = 32
phone = 8860879079
email = "aditya.varshneya@gmail.com"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
content = [10, 20, 30, 40, 50, 60, 70, 90, 100, 110, 120, 80, 23, 23, 130, 22]
keys = ["From 2 years", "From 7 Years", "Mild Symptoms", "chronic symptoms", "Severity high"]


# code elements
@pytest.mark.flaky(rerun=1)
def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window()
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
def test_login():
    global driver
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click()
    driver.save_screenshot("./screenshots/test_logindoc/login.png")
    time.sleep(7)


#@pytest.mark.skip
@pytest.mark.flaky(rerun=1)
def test_doc_reg():
    wait = WebDriverWait(driver, 30, 2)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click()
    time.sleep(3)
    driver.find_element_by_id("optionsRadios1").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click()
    time.sleep(3)
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(age)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div["
        "1]/div/label/input").click()
    driver.find_element_by_id("email").send_keys(email)
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click()
    time.sleep(8)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    time.sleep(8)
    driver.save_screenshot("./screenshots/test_logindoc/appt.png")
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[2]/div").click()
    driver.back()
    time.sleep(3)


# @pytest.mark.skip
@pytest.mark.flaky(rerun=1)
def test_verify_form_template():
    wait = WebDriverWait(driver, 30, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH,
                                                 "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
                                                 "1]/div/div/div[1]/div/div[1]/div/div[2]"))).click()
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[2]").click()
    time.sleep(10)
    wait = WebDriverWait(driver, 10, 2)
    add = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/a[1]/span")))
    add.click()
    time.sleep(5)
    driver.save_screenshot("./screenshots/test_logindoc/template.png")
    try:
        button_add = driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/table/tr/td[3]/span")
        if button_add.is_displayed():
            button_add.click()
    except:
        pass
    time.sleep(5)
    checkboxes = driver.find_elements_by_id("value")
    for checkbox in checkboxes:
        if checkbox.is_displayed( ):
            checkbox.send_keys(random.choice(content))
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,-3500)", "")
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//*[@id='collapse-13']/div/div/div/div[2]/div/div/div[1]").click()
        for complaint in range(1, 5):
            complaint = driver.find_element_by_xpath(
                "//*[@id='sidebar-wrapper']/div/div/button[" + str(complaint) + "]")
            complaint.click()
    except NoSuchElementException:
        pass
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,500)", "")
    time.sleep(3)
    driver.save_screenshot("./screenshots/test_logindoc/template2.png")
    driver.find_element_by_xpath(
        "//*[@id='content']/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/button").click()

    driver.execute_script("window.scrollBy(0,-4500)", "")
    time.sleep(11)
    date_format = driver.find_element_by_xpath(
        '//*[@id="content"]/span[1]/div/div/div/div/div[3]/div/div[1]/div/div[2]/div/span')
    # print(date_format)
    date_time = (date_format.text).split(' ')
    time_format = (date_time[4].split('\n'))
    print(time_format, str(datetime.datetime.today().strftime("%H:%M")))
    # utc_now = datetime.datetime.utcnow()
    try:
        assert (time_format[0]) == (str(datetime.datetime.today().strftime("%H:%M")))
    except:
        my_time = datetime.datetime.today()
        duration = datetime.timedelta(minutes=1)
        current_time = (my_time - duration)
        pres_time = (current_time.strftime("%H:%M"))
        assert (time_format[0]) == pres_time
    # (utc_now.strftime("%H:%M"))
    time.sleep(3)


@pytest.mark.skip
@pytest.mark.flaky(rerun=1)
def test_verify_presc_upload():
    wait = WebDriverWait(driver, 30, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/a[2]/span'))).click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,400)", "")
    time.sleep(10)
    try:
        upload = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div/span[3]/"
                                              "div/div/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div["
                                              "1]/form/div/input")
        upload.send_keys('C:/Users/Lenovo/Desktop/Python/file.png')

    except:
        driver.find_element_by_xpath("//*[@id='#']/div/input").send_keys(
            'C:/Users/Lenovo/Desktop/Python/file.png')
    driver.save_screenshot("./screenshots/test_logindoc/prescupload.png")
    time.sleep(4)
    try:
        driver.find_element_by_xpath(
            "//*[@id='printmodal']/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[4]/div/button[1]").click()
    except:
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div/span/div/div/div[3]/div/div/div[2]/div/div["
            "1]/div/div/div/div/div[2]/div[4]/div/button[1]").click()
    time.sleep(10)
    date_format_p = driver.find_element_by_xpath('//*[@id="content"]/span[1]/div/div/div/div/div[1]/div/div[1]/div/div['
                                                 '2]/div/span')
    # print(date_format)
    date_time_p = date_format_p.text.split(' ')
    time_format_p = (date_time_p[4].split('\n'))
    print(time_format_p, str(datetime.datetime.today().strftime("%H:%M")))
    # utc_now = datetime.datetime.utcnow()
    try:
        assert (time_format_p[0]) == (str(datetime.datetime.today().strftime("%H:%M")))
    except:
        my_time_p = datetime.datetime.today()
        duration_p = datetime.timedelta(minutes=1)
        current_time = (my_time_p - duration_p)
        pres_time_p = (current_time.strftime("%H:%M"))
        assert (time_format_p[0]) == pres_time_p
    time.sleep(3)


#@pytest.mark.skip
@pytest.mark.flaky(rerun=1)
def test_verify_patient_upload():
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[5]/div").click()
    time.sleep(3)
    try:
        card_title = driver.find_element_by_xpath("//*[@id='patient']/div/div/div/div[2]/div[2]/div/div[1]/h4")
        if card_title.is_displayed():
            assert True
        else:
            assert "No Patient uploads"
        # time_format = driver.find_element_by_xpath('//*[@id="patient"]/div/div/div/div[2]/div[1]/div/div[2]/div/span')
        # time_1 = (time_format.text).split(',')
        # print(time_1)
        # utc_now = datetime.datetime.utcnow()
        # assert (time_1[1]) == (utc_now.strftime("%H:%M"))
        # (str(datetime.datetime.today().strftime("%H:%M")))
    except NoSuchElementException:
        driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[6]/a/i").click()

    driver.save_screenshot("./screenshots/test_logindoc/upload.png")
    time.sleep(7)
    # driver.find_element_by_xpath("/html/body/div/div/div/div/div[6]/a/i").click()
    # time.sleep(5)
    driver.back()
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
def test_verify_case_history():
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 30, 2)
    status_booked = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div["
                                                                           "2]/div/div/div[1]/div/div/div["
                                                                           "1]/div/div/div[1]/div/div[1]/div/div[2]")))
    status_booked.click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div["
                                 "2]/table/tbody/tr[1]/td[7]/button[2]").click()
    time.sleep(5)
    driver.save_screenshot("./screenshots/test_logindoc/case1.png")
    try:
        case_history_link = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[1]/div/div[2]/p/a")
        if case_history_link.is_displayed( ):
            driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[4]/div").click()  ## Case History header
        else:
            print("Case history already written")
    except NoSuchElementException:
        driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[4]/div").click()
    time.sleep(3)
    drop_down = driver.find_element_by_xpath("//*[@id='heading-13']/a/h6")
    driver.save_screenshot("./screenshots/test_logindoc/casehistory1.png")
    try:
        if drop_down:
            time.sleep(4)
            socio_var = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/"
                                                     "div/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/select")

            drp = Select(socio_var)
            drp.select_by_value("Upper")

            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='collapse-13']/div/div[2]/div/div[2]/input").clear()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='collapse-13']/div/div[2]/div/div[2]/input").send_keys(
                "Patient has smoking habit")
            time.sleep(1)
            both = "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div[" \
                   "1]/div/div[1]/label/input"
            veg = "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div[" \
                  "1]/div/div[2]/label/input "
            non_veg = "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/div[" \
                      "3]/div/div[" \
                      "1]/div/div[3]/label/input "
            driver.find_element_by_xpath(random.choice([both, veg, non_veg])).click( )
            time.sleep(1)
            no_meals = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/div/div/"
                                                    "div/div[1]/div/div[2]/div[2]/div/div[4]/div/div[2]/input")

            no_meals.clear( )
            time.sleep(1)
            no_meals.send_keys(random.choice(keys))
            time.sleep(1)
            k_cal = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/div/div/div/"
                                                 "div[1]/div/div[2]/div[2]/div/div[5]/div/div[2]/input")
            k_cal.clear()
            time.sleep(1)
            k_cal.send_keys(random.choice(keys))
            time.sleep(1)
            '''
            physical Activity
            '''
            sedentry = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]"
                                                    "/div/div[2]/div[2]/div/div[6]/div/div[1]/div/div[1]/label/input")
            mild = driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/"
                "div[2]/div/div[6]/div/div[1]/div/div[2]/label/input")
            moderate = driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/"
                "div[2]/div/div[6]/div/div[1]/div/div[3]/label/input")
            heavy = driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/"
                "div[2]/div/div[6]/div/div[1]/div/div[4]/label/input")
            random.choice([sedentry, mild, moderate, heavy]).click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/"
                                         "div/div[2]/div[2]/div/div[7]/div/div[1]/div/div[1]/label/input").click()
    except NoSuchElementException or ElementNotInteractableException:
        if drop_down.is_displayed():
            drop_down.click()
            socio_var = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/"
                                                     "div/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/select")
            drp = Select(socio_var)
            drp.select_by_value("Upper")

            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='collapse-13']/div/div[2]/div/div[2]/input").clear()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='collapse-13']/div/div[2]/div/div[2]/input").send_keys(
                "Patient has smoking habit")
            time.sleep(1)
            both = "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div[" \
                   "1]/div/div[1]/label/input "
            veg = "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[2]/label/input"
            non_veg = "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div[" \
                      "1]/div/div[3]/label/input "
            driver.find_element_by_xpath(random.choice([both, veg, non_veg])).click()
            time.sleep(1)
            no_meals = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/div/div/"
                                                    "div/div[1]/div/div[2]/div[2]/div/div[4]/div/div[2]/input")
            time.sleep(1)
            no_meals.clear()
            time.sleep(1)
            no_meals.send_keys(random.choice(keys))
            time.sleep(1)
            k_cal = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/div/div/div/"
                                                 "div[1]/div/div[2]/div[2]/div/div[5]/div/div[2]/input")
            k_cal.clear()
            time.sleep(1)
            k_cal.send_keys(random.choice(keys))
            time.sleep(1)
            '''
            physical Activity
            '''
            sedentry = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]"
                                                    "/div/div[2]/div[2]/div/div[6]/div/div[1]/div/div[1]/label/input")
            mild = driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/"
                "div[2]/div/div[6]/div/div[1]/div/div[2]/label/input")
            moderate = driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/"
                "div[2]/div/div[6]/div/div[1]/div/div[3]/label/input")
            heavy = driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/div/div[2]/"
                "div[2]/div/div[6]/div/div[1]/div/div[4]/label/input")
            random.choice([sedentry, mild, moderate, heavy]).click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[4]/div/div/div/div[1]/"
                                         "div/div[2]/div[2]/div/div[7]/div/div[1]/div/div[1]/label/input").click()
        else:
            driver.find_element_by_xpath("//*[@id='heading-13']/a/h6").click()
            time.sleep(2)
    comment = driver.find_elements_by_name("comment")
    for comm in comment:
        if comm.is_displayed():
            comm.clear()
            time.sleep(1)
    for comm in comment:
        if comm.is_displayed():
            time.sleep(1)
            comm.send_keys(random.choice(keys))
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='casehistory']/div/div/div/div[2]/button").click()
    ## Submit Button
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='casehistory']/div[2]/div[2]/p/span/button").click()
    time.sleep(3)
    driver.save_screenshot("./screenshots/test_logindoc/casehistory3.png")
    driver.back()
    time.sleep(3)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_verify_case_history"])
def test_verify_case():
    wait = WebDriverWait(driver, 30, 2)
    status_booked = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/div/div["
                                                                           "2]/div/div/div[1]/div/div/div["
                                                                           "1]/div/div/div[1]/div/div[1]/div/div[2]")))
    status_booked.click()
    driver.save_screenshot("./screenshots/test_logindoc/case.png")
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div["
                                 "2]/table/tbody/tr[1]/td[7]/button[2]").click()
    time.sleep(5)
    case_history = driver.find_element_by_xpath("//*[@id='accordion-5']/div[1]/div/div/div[2]")
    assert case_history.is_displayed(), True
    time.sleep(3)
    driver.back()
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
@pytest.mark.dependency(depends=["test_verify_case_history"])
def test_verify_reschedule():
    wait = WebDriverWait(driver, 20, 2)
    status_booked = wait.until(EC.visibility_of_element_located(
        (
            By.XPATH,
            "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]")))
    status_booked.click()
    driver.save_screenshot("./screenshots/test_logindoc/rescheule.png")
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[1]").click()
    time.sleep(4)
    reschedule = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/button[3]")
    reschedule.click( )
    time.sleep(5)
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/section/div[2]/div/div/div[2]/div/div["
        "1]/div/button[1]").click()
    time.sleep(3)
    driver.find_element_by_name("rescheduleRemarks").send_keys("Doctor not available")
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/section/div[5]/div/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span[2]/button").click()
    time.sleep(7)
    driver.implicitly_wait(20)
    driver.save_screenshot("./screenshots/test_logindoc/reschedule2.png")
    driver.find_element_by_xpath("//*[@id='root']/div[1]/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    time.sleep(3)
    driver.back()
    time.sleep(5)

    driver.close()
