import random
import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# parameters
username = 8860879079
password = "Pass@12345"
name = "Testing Automate"
ip_url = "https://clinytics.hlthclub.in/doctor-login"
content = [10, 20, 30, 40, 50, 60, 70, 90, 100, 110, 120, 80, 36, 34, 130, 32, 97]


@pytest.mark.flaky(rerun=1)
def test_setup():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(ip_url)
    driver.delete_all_cookies()
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
def test_add_new_template():  ## create new template
    try:
        time.sleep(5)
        while False:
            WebDriverWait(driver,30,3).until(EC.visibility_of_element_located((By.XPATH,
                                                                                 "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
                                                                                 "1]/div/div/div[1]/div/div[1]/div/div[2]"))).click()
        time.sleep(2)
        booked = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/"
                                              "div/div/div[2]/table/tbody/tr/td[7]/button[2]")
        if booked.is_displayed():
            booked.click()
        else:
            print("Booked Appointment not Available")
    except NoSuchElementException:
        driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/"
                                     "div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()
        done = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/"
                                            "div/div/div[2]/table/tbody/tr[1]/td[5]/label").text
        assert "Done" in done, "appointment not available"
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/"
                                     "div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[2]").click()
    time.sleep(5)
    try:
        wait = WebDriverWait(driver, 30)
        add = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/a[1]/span")))
        add.click()
    except:
        pass
    time.sleep(3)
    try:
        template_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/"
                                                       "table/tr/td[3]/span")
        if template_button.is_displayed():
            template_button.click()
    except:
        pass
    time.sleep(5)
    checkboxes = driver.find_elements_by_xpath("//*[@id='value']")
    for checkbox in checkboxes:
        if checkbox.is_displayed():
            checkbox.send_keys(random.choice(content))
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,-4500)", "")
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//*[@id='collapse-13']/div/div/div/div[1]/div/div/div[1]/div[1]").click()
        for complaint in range(1, 5):
            complaint = driver.find_element_by_xpath(
                "//*[@id='sidebar-wrapper']/div/div/button[" + str(complaint) + "]")
            complaint.click()
    except NoSuchElementException:
        pass
    time.sleep(4)
    driver.execute_script("window.scrollBy(0,-3500)", "")
    time.sleep(5)
    driver.find_element_by_id("dropdownMenuSizeButton3").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[2]/div/a[1]").click()
    new = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[2]/button[1]")
    new.click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@placeholder='Enter template name']").send_keys("Instant Prescription")
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[3]/button").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[2]/div[2]/p/span/button").click()
    time.sleep(7)
    driver.find_element_by_xpath(
        "//*[@id='content']/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/button").click()
    time.sleep(2)
    driver.back()
    time.sleep(5)


@pytest.mark.flaky(rerun=1)
def test_verify_quick_tools():  ## check quick tools/ verify template in local
    try:
        wait = WebDriverWait(driver, 40, 2)
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     "//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div["
                                                     "1]/div/div/div[1]/div/div[1]/div/div[2]"))).click()
        booked = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/"
                                              "div/div/div[2]/table/tbody/tr/td[7]/button[2]")
        if booked.is_displayed():
            booked.click()
        else:
            print("Booked Appointment not Available")
    except NoSuchElementException:
        driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/"
                                     "div/div[1]/div/div/div[1]/div/div[1]/div/div[4]").click()
        done = driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div/div[1]/"
                                            "div/div/div[2]/table/tbody/tr[1]/td[5]/label").text
        assert "Done" in done, "appointment not available"
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/"
                                     "div/div[1]/div/div/div[2]/table/tbody/tr[1]/td[7]/button[2]").click()
    time.sleep(5)
    try:
        wait = WebDriverWait(driver, 20, 2)
        add = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/a[1]/span")))
        add.click()
    except:
        pass
    time.sleep(3)
    try:
        template_button = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div/div[1]/"
                                                       "table/tr/td[3]/span")
        if template_button.is_displayed():
            template_button.click()
    except:
        pass
    time.sleep(3)
    try:
        button_add = driver.find_element_by_xpath("//*[@id='dropdownMenuSizeButton3']")
        quick_text = driver.find_element_by_id("dropdownMenuSizeButton3").text
        assert " Quick Tools " in quick_text, "Text is not correct"
        if button_add.is_displayed():
            button_add.click()
    except:
        driver.find_element_by_xpath("//*[@id='dropdownMenuSizeButton3']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[2]/div/a[2]").click()
    time.sleep(3)
    template_name = len(driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div/table/tr/td[2]"))
    print("count of total template", template_name)
    for temp in range(1, template_name + 1):
        var = driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div/div/div[" + str(temp) + "]/table/tr/td[2]").text
        print(var)
        if "Instant Prescription" in var:
            print("Template exist")
        else:
            print("Template not exist")
    time.sleep(2)
    driver.find_element_by_xpath("html/body/div[3]/div/div/div[1]/button/span[1]").click()
    time.sleep(3)


@pytest.mark.flaky(rerun=1)
def test_existing_template():  ## use local prescription to upload and verify
    driver.find_element_by_id("dropdownMenuSizeButton3").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div/div[2]/div/a[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/table/tr/td[3]/span").click()
    time.sleep(4)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[2]/div[2]/div[2]/p/span").click()  ## Loaded instant prescription
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='content']/div[2]/div/div/div/div/div/"
                                 "div/div/div/div[1]/div/div[3]/button").click()
    time.sleep(4)
    driver.close()
