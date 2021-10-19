import time

from numpy import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Parameters
mobile = "9582944108"
ip_site = "https://betaclinytics.hlthclub.in/ckbirlabfi/consult-online"


# code element
t = 0
while t < 10:
    chrome_options = webdriver.ChromeOptions( )
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options=chrome_options)
    driver.get(ip_site)
    driver.maximize_window( )
    driver.delete_all_cookies( )
    time.sleep(5)


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
    driver.find_element_by_xpath("//*[@id='root']/div/div/section[1]/div/div/div/div/div[2]/form/div[3]/button").click( )
    time.sleep(8)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/section[1]/div/div/div/div/div[2]/div/div[2]/p/span/button").click( )
    # registration button

    time.sleep(7)

    xpath = ["//*[@id='root']/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[5]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[6]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[7]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[8]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[11]/div[1]/div[2]/div/div[2]/a",
             "//*[@id='root']/div/div/div/div/div/div/div[2]/div[10]/div[1]/div[2]/div/div[2]/a"]

    driver.find_element_by_xpath(random.choice(xpath)).click()
    # Book Appointment Button
    time.sleep(5)
    time_slot = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[2]/div/"
                                             "div[1]/div[2]/section/div[3]/div/div/div[2]/div/div[1]/div/button[1]")  # time slot selection
    if time_slot.is_displayed( ):
        time_slot.click( )
    else:
        driver.find_element_by_xpath("//*[@id='timeslotmodal']/div/div[1]/div[2]/section/"
                                     "div[3]/div/div/div[1]/div/div/div/ul/li[9]/a/i").click( )
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='timeslotmodal']/div/div[1]/div[3]/button[2]").click( )
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/p/span/button").click( )
    time.sleep(20)
    print("Appointment booked, kindly make payment or go to chatroom link")
    print("Please run Patient_checkin file")
    time.sleep(3)
    driver.close()
    t=+1