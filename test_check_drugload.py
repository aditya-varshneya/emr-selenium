import random
import time
from datetime import datetime
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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


# code elements
@pytest.mark.flaky(rerun=1)
def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions( )
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.maximize_window( )


@pytest.mark.flaky(rerun=1)
def test_login():
    global driver
    username_textbox = driver.find_element_by_id("exampleInputUsername")
    username_textbox.send_keys(username)
    password_textbox = driver.find_element_by_id("exampleInputUserpassword")
    password_textbox.send_keys(password)
    login_but = driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div/div/div/div/div/div/div[3]/div/form/div[3]/button")
    login_but.click( )
    time.sleep(7)


@pytest.mark.flaky(rerun=1)
# @pytest.mark.skip
def test_doc_reg():
    wait = WebDriverWait(driver, 35, 2)
    add = wait.until(EC.visibility_of_element_located((By.ID, "settings-trigger")))
    add.click( )
    time.sleep(3)
    driver.find_element_by_id("optionsRadios1").click( )
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/button").click( )
    time.sleep(3)
    driver.find_element_by_id("name").send_keys(name)
    driver.find_element_by_id("age").send_keys(age)
    driver.find_element_by_id("phone").send_keys(phone)
    driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[6]/div[2]/div/div/div/div["
        "1]/div/label/input").click( )
    driver.find_element_by_id("email").send_keys(email)
    time.sleep(4)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div/div/div/div/div/div/form/div[13]/div/div/div/button").click( )
    time.sleep(15)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div[2]/div[2]/p/span/button").click( )
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='horizontal-top-example']/li[2]/div").click( )
    time.sleep(3)
    driver.back( )
    time.sleep(10)
    driver.save_screenshot("./screenshots/test_logindoc/drugsave.png")


# @pytest.mark.flaky(rerun=1)
# @pytest.mark.skip
def test_verify_drug_save():
    driver.delete_all_cookies( )
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]").click( )
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[2]").click( )
    time.sleep(5)
    WebDriverWait(driver, 40, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/a["
                                                                                   "1]/span"))).click( )
    time.sleep(5)
    driver.save_screenshot("./screenshots/test_logindoc/drugsave1.png")
    try:
        button_add = driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/table/tr/td[3]/span")
        if button_add.is_displayed( ):
            button_add.click( )
    except:
        pass
        time.sleep(5)
    driver.execute_script("window.scrollBy(0,-400)", "")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='collapse-13']/div/div/div/div[2]/div/div/div[1]/div[1]").click( )
    for drug in range(1, 5):
        drugs = driver.find_element_by_xpath("//*[@id='sidebar-wrapper']/div/div/button[" + str(drug) + "]")
        drugs.click( )
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='Drugs']/nav/ul/li[1]/a").click( )
    time.sleep(1)
    drug_name = driver.find_element_by_name("groupName")
    drug_name.send_keys("Drug list 3")
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[2]/button").click( )
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div/div/div/div/div/div/div/div[1]/"
                                 "div[1]/div[2]/p/span[2]/button").click( )
    time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='content']/div[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/p/span/button").click( )
    time.sleep(7)
    driver.find_element_by_xpath(
        "//*[@id='content']/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/button").click( )

    time.sleep(5)


@pytest.mark.flaky(rerun=1)
# @pytest.mark.skip
def test_verify_drug_load():
    driver.delete_all_cookies( )
    add = WebDriverWait(driver, 30, 2).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/a[1]/span")))
    add.click( )
    time.sleep(5)
    try:
        button_add = driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/table/tr/td[3]/span")
        if button_add.is_displayed( ):
            button_add.click( )
    except:
        pass
        time.sleep(5)
    driver.execute_script("window.scrollBy(0,-2200)", "")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='Drugs']/nav/ul/li[2]/a").click( )
    time.sleep(8)
    try:
        list_name = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/div").text
        assert list_name == 'Drug list 3', "list not present"
    except:
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/button").click( )
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div/div[1]/div[2]/button").click( )
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='content']/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/button").click( )
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,-3500)", "")
    time.sleep(2)
    driver.save_screenshot("C:\\Users\\Lenovo\\Documents\\GitHub\\emr-selenium-automation\\"
                           "jenkins\\screenshots\\test_drug_load\\drug_view.png")


@pytest.mark.flaky(rerun=1)
def test_drug_verification():
    # try:
    #     wait = WebDriverWait(driver, 30, 2)
    #     wait.until(EC.visibility_of_element_located((By.XPATH,
    #                                                  "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
    #                                                  "1]/div/div/div[1]/div/div[1]/div/div[2]"))).click()
    #     time.sleep(2)
    #     booked = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/"
    #                                           "div/div/div[2]/table/tbody/tr/td[7]/button[2]")
    #     if booked.is_displayed():
    #         booked.click()
    #     else:
    #         print("Booked Appointment not Available")
    # except NoSuchElementException:
    #     driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/"
    #                                  "div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()
    #     done = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/"
    #                                         "div/div/div[2]/table/tbody/tr[1]/td[5]/label").text
    #     assert "Done" in done, "appointment not available"
    #     time.sleep(2)
    #     driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/"
    #                                  "div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[2]").click()
    # time.sleep(5)
    # Drug Value check in preview page ##
    driver.execute_script("window.scrollBy(0,400)", "")
    presc_1 = len(driver.find_elements_by_xpath("//*[@id='content']/span[1]/div/div/div/div/div[3]/div/div[2]/div/div/"
                                                "div/div/div/div/div/div/div/div/div/div/table/tbody/tr"))

    presc_2 = len(driver.find_elements_by_xpath("//*[@id='content']/span[2]/div/div/div/div/div[3]/div/"
                                                "div[2]/div/div/div/div/div/div/div/div/div/div/div/div/table/tbody/tr"))
    drug_table1 = []
    drug_table2 = []
    for status in range(1, presc_1):
        drug_first = driver.find_element_by_xpath(
            "//*[@id='content']/span[1]/div/div/div/div/div[3]/div/div[2]/div/div/"
            "div/div/div/div/div/div/div/div/div/div/table/tbody/tr[" + str(
                status) + "]").text
        drug_table1.append(drug_first)
    print(drug_table1)
    time.sleep(3)
    for status_1 in range(1, presc_2):
        time.sleep(2)
        drug_second = driver.find_element_by_xpath("//*[@id='content']/span[2]/div/div/div/div/"
                                                   "div[3]/div/div[2]/div/div/div/div/"
                                                   "div/div/div/div/div/div/div/div/table/tbody/tr[" + str(
            status_1) + "]").text
        drug_table2.append(drug_second)
    print(drug_table2)
    assert random.choice(drug_table1) in drug_table2, "Condition not satisfy"
    driver.close( )
