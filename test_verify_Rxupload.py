import random
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
diagnosis = ["Hypertension,Hyperlipidemia,Diabetes,Anxiety,Obesity,Allergic rhinitis,Reflux esophagitis"]
complaints = ["Back pain,Fever,Headache,Visual Impairment"]
investigation = ["CBC,SGPT,SGOT,HB1Ac,Serum Creatinine,Uric Acid"]


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
    time.sleep(7)


@pytest.mark.flaky(rerun=1)
#@pytest.mark.skip
def test_doc_reg():
    wait = WebDriverWait(driver, 40, 2)
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
    time.sleep(8)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[2]/div").click()
    driver.back()
    time.sleep(3)


@pytest.mark.flaky(rerun=1)
# @pytest.mark.skip
def test_Rxupload():
    wait = WebDriverWait(driver, 30, 2)
    wait.until(EC.visibility_of_element_located((By.ID, "profileDropdown"))).click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/nav/div[2]/ul[2]/li/div/a[2]").click()

    time.sleep(5)


@pytest.mark.flaky(rerun=1)
# @pytest.mark.skip
def test_Rxupload_diagnosis():
    ## diagnosis
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div[1]/div/div[4]/div/div/div/div/div[5]/div/div/div/p/a").click()

    time.sleep(3)
    rx_dropdown = driver.find_element_by_name("type")
    select = Select(rx_dropdown)
    select.select_by_value("diagnosis")
    time.sleep(2)
    driver.find_element_by_name("branches").send_keys(diagnosis)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[3]/div[2]/p/span/button").click()


@pytest.mark.flaky(rerun=1)
# @pytest.mark.skip
def test_Rxupload_complaint():
    ## complaints
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div[1]/div/div[4]/div/div/div/div/div[5]/div/div/div/p/a").click()
    time.sleep(3)
    rx_dropdown = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/select")
    select = Select(rx_dropdown)
    select.select_by_value("complaints")
    time.sleep(2)
    driver.find_element_by_name("branches").send_keys(complaints)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[3]/div[2]/p/span/button").click()


@pytest.mark.flaky(rerun=1)
# @pytest.mark.skip
def test_Rxupload_investigation():
    ## investigations
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div[1]/div/div[4]/div/div/div/div/div[5]/div/div/div/p/a").click()
    time.sleep(3)
    rx_dropdown = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/select")
    select = Select(rx_dropdown)
    select.select_by_value("investigations")
    time.sleep(2)
    driver.find_element_by_name("branches").send_keys(investigation)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[3]/div[2]/p/span/button").click()


@pytest.mark.flaky(rerun=1)
# @pytest.mark.skip
def test_Rxupload_drugs():
    ## drugs
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div[1]/div/div[4]/div/div/div/div/div[5]/div/div/div/p/a").click()
    time.sleep(3)
    rx_dropdown = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/select")
    select = Select(rx_dropdown)
    select.select_by_value("drugs")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='#']/div/input").send_keys(
        "C:/Users/Lenovo/Documents/GitHub/emr-selenium-automation/jenkins/drugs.tsv")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[3]/div[2]/p/span/button").click()
    time.sleep(2)
    driver.back()


@pytest.mark.flaky(rerun=1)
def test_verify_Rxupload():
    wait = WebDriverWait(driver, 30, 2)
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
                                                     "1]/div/div/div[1]/div/div[1]/div/div[2]"))).click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[2]").click()

    except:
        driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/"
                                     "div/div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()

        time.sleep(3)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td["
            "7]/button[2]").click()

    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/a[1]/span").click()
    time.sleep(2)
    try:
        template_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/"
                                                       "table/tr/td[3]/span")
        if template_button.is_displayed():
            template_button.click()
    except:
        pass
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
def test_verify_complaint():
    global complaint_sidebox, comp, c_status
    complaint_list = ["Back pain", "Fever", "Headache", "Visual Impairment"]
    complaints_1 = random.choice(complaint_list)
    print("The random choice is {}".format(complaints_1))
    try:
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/"
            "div/div/div/div[1]/div/div[2]/div/div[3]/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]").click()

    except:
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/div/div/"
            "div/div[1]/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]"
        ).click()
    time.sleep(2)
    complaint_box = len(driver.find_elements_by_xpath("//*[@id='sidebar-wrapper']/div/div/button"))
    for complaint in range(1, complaint_box + 1):
        try:
            complaint_sidebox = driver.find_element_by_xpath(
                "//*[@id='sidebar-wrapper']/div/div/button[" + str(complaint) + "]").text
            status_1 = list(complaint_sidebox.split(" , "))
            print(status_1, end='     ')
            time.sleep(2)
            if complaints_1 in status_1:
                print("Value Exist")
            else:
                print(status_1, end='     ')
                raise ValueError("Value doesn't Exists")
        except:
            pass
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
def test_verify_diagnosis():
    global diagnosis_sidebox
    diagnosis_list = ["Hypertension", "Hyperlipidemia", "Diabetes", "Anxiety", "Obesity", "Allergic Rhinitis",
                      "Reflux Esophagitis"]
    diagnosis_1 = random.choice(diagnosis_list)
    print("The random choice is {}".format(diagnosis_1))
    try:
        ## RX template (drop down selection)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/"
            "div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[1]/div/div/div[1]").click()
    except:
        ## General template (auto type header)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/"
            "div[1]/div/div[1]/div/div[5]/div[2]/div/div/div/div[1]/div/div/div[1]").click()
    diagnosis_box = len(driver.find_elements_by_xpath("//*[@id='sidebar-wrapper']/div/div/button"))
    for diagnose in range(1, diagnosis_box + 1):
        try:
            diagnosis_sidebox = driver.find_element_by_xpath(
                "//*[@id='sidebar-wrapper']/div/div/button[" + str(diagnose) + "]").text
            print(diagnosis_sidebox)
            status = list(diagnosis_sidebox.split(" , "))
            print(status, end='     ')
            time.sleep(2)
            if diagnosis_1 in status:
                print("Value Exist")
            else:
                print(status, end='     ')
                raise ValueError("Value doesn't Exist")
        except:
            pass
    time.sleep(3)


@pytest.mark.flaky(rerun=1)
def test_verify_investigations():
    global investigation_sidebox
    investigation_list = ["CBC", "SGPT", "SGOT", "HB1Ac", "Serum Creatinine", "Uric Acid"]
    investigation_1 = random.choice(investigation_list)
    print("The random choice is {}".format(investigation_1))
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/div/"
        "div/div/div[1]/div/div[2]/div/div[8]/div[2]/div/div/div/div[1]/div[1]/input").click()
    time.sleep(2)
    investigation_box = len(driver.find_elements_by_xpath("//*[@id='sidebar-wrapper']/div/div/button"))
    for invest in range(1, investigation_box + 1):
        try:
            investigation_sidebox = driver.find_element_by_xpath(
                "//*[@id='sidebar-wrapper']/div/div/button[" + str(invest) + "]").text
            status_2 = list(investigation_sidebox.split(" , "))
            print(status_2, end='     ')
            time.sleep(2)
            if investigation_1 in status_2:
                print("Value Exist")
            else:
                print(status_2, end='     ')
                raise ValueError("Value doesn't Exists")
        except:
            pass
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
def test_verify_drugs():
    global drug_sidebox
    drugs_list = ["Amoxyiclav", "Calpol", "Ultracet", "Incidil", "Becasules"]
    drugs_1 = random.choice(drugs_list)
    print("The random choice is {}".format(drugs_1))
    try:
        ## RX template (drop down selection)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/div/div/"
            "div/div[1]/div/div[2]/div/div[6]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]").click()
    except:
        ## General template (auto type header)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div/div/div/"
            "div/div[1]/div/div[1]/div/div[6]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]"
        ).click()

    time.sleep(2)
    drug_box = len(driver.find_elements_by_xpath("//*[@id='sidebar-wrapper']/div/div/button"))
    time.sleep(2)
    for drg in range(1, drug_box + 1):
        try:
            drug_sidebox = driver.find_element_by_xpath(
                "//*[@id='sidebar-wrapper']/div/div/button[" + str(drg) + "]").text
            status_drug = list(drug_sidebox.split(" , "))
            print(status_drug, end='     ')
            time.sleep(2)
            if drugs_1 in status_drug:
                print("Value Exist")
            else:
                print(status_drug, end='  ')
                raise ValueError("Value doesn't Exists")
        except:
            pass
    time.sleep(3)
    driver.close()
