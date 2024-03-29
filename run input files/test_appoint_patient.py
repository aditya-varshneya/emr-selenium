import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Parameters
mobile = "8860879079"
ip_site = "https://clinytics.hlthclub.in/new_demo_account/consult-online"


# code element
def test_reg():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=chrome_options)
    driver.get(ip_site)
    driver.maximize_window()
    driver.delete_all_cookies()
    time.sleep(5)


def test_verify_card():
    details = driver.find_element_by_xpath("/html/body/div/div/div/section[1]/div/div/div/div/div[1]/h4").text
    assert "New Demo Account " in details, "test passed"
    time.sleep(3)
    logo = driver.find_element_by_xpath("//*[@id='root']/div/div/section[1]/div/div[1]/a/div/div/img").is_displayed()
    if logo == True:
        assert True
    else:
        assert "logo is not available"


def test_fill_form():
    driver.find_element_by_name("name").send_keys("Automation Test")
    driver.find_element_by_name("age:no_of_years").send_keys("33")
    element = driver.find_element_by_name("gender")
    drp = Select(element)
    drp.select_by_value("male")
    driver.find_element_by_name("email").send_keys("aditya.varshneya@gmail.com")
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/section[1]/div/div/div/div/div[2]/form/div[1]/div[5]/div/div/div/div/input").send_keys(
        mobile)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='root']/div/div/section[1]/div/div/div/div/div[2]/form/div[3]/button").click()
    time.sleep(8)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/section[1]/div/div/div/div/div[2]/div/div[2]/p/span/button").click()
    # registration button
    try:
        otp = driver.find_element_by_name("otp")
        if otp.is_displayed():
            get_otp = input("Enter OTP: ")
            otp.send_keys(get_otp)
    except NoSuchElementException:
        pass

    time.sleep(7)


def test_doctor_appoint():
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div[2]/div[7]/div[1]/div[2]/div/div[2]/a").click()
    # Book Appointment Button
    time.sleep(5)
    time_slot = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[2]/div/"
                                             "div[1]/div[2]/section/div[3]/div/div/div[2]/div/div[1]/div/button[1]")  # time slot selection
    if time_slot.is_displayed():
        time_slot.click()
    else:
        driver.find_element_by_xpath("//*[@id='timeslotmodal']/div/div[1]/div[2]/section/"
                                     "div[3]/div/div/div[1]/div/div/div/ul/li[9]/a/i").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='timeslotmodal']/div/div[1]/div[3]/button[2]").click()
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/p/span/button").click()
    time.sleep(15)
    print("Appointment booked, kindly make payment or go to chatroom link")
    print("Please run Patient_checkin file")
    time.sleep(3)

def test_verify_paymentlink():
    try:
        time.sleep(15)
        link  = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/"
                                                           "div/div/div/div[2]/button/a/h4")
        if link.is_displayed():
            print("payment link working fine")
        else:
            print ("Redirection not working")
        time.sleep(3)
        redirection_link = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div[2]/button/a/p")
        redirection_text = redirection_link.text
        assert "Please click here to make payment" in redirection_text
        time.sleep(2)
        redirection_link.click()
    except:
        payment = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div[2]/button/a/p[2]").text
        assert "Please click here to start your Consultation" in payment
        text = driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div/div/div/div/div[2]/button/a/p[1]").text
        assert "Tele Consultation Link" in text
    time.sleep(3)
    driver.minimize_window()
    driver.close()
