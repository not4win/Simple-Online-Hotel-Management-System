#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


#in main page
driver = webdriver.Chrome(executable_path='/home/ashwin/ashwinx/newcoding/se/Online-Hotel-Management-System-master/automation/chromedriver')
driver.set_window_size(1920,1080)
driver.get("http://localhost:5000")

#going to rooms page
elem = driver.find_element_by_id("rooms")
time.sleep(3)
elem.click()

#Clicking on free rooms
elem = driver.find_element_by_id("green")
time.sleep(3)
elem.click()

#Filling the form
name="Ashwin"
count = "4"
email = "ashwin@gmail.com"
streetno = "7"
city = "Mysore"
country = "India"
state = "Karnataka"
pincode = "575001"
check_in = "03/03/2019"
check_out = "05/05/2019"

elem = driver.find_element_by_id("check_in")
elem.send_keys(check_in)
time.sleep(1)

elem = driver.find_element_by_id("check_out")
elem.send_keys(check_out)
time.sleep(1)

elem = driver.find_element_by_id("name")
elem.send_keys(name)
time.sleep(1)

elem = driver.find_element_by_id("count")
elem.send_keys(count)
time.sleep(1)

elem = driver.find_element_by_id("email")
elem.send_keys(email)
time.sleep(1)

elem = driver.find_element_by_id("streetno")
elem.send_keys(streetno)
time.sleep(1)

elem = driver.find_element_by_id("city")
elem.send_keys(city)
time.sleep(1)

elem = driver.find_element_by_id("country")
elem.send_keys(country)
time.sleep(1)

elem = driver.find_element_by_id("state")
elem.send_keys(state)
time.sleep(1)

elem = driver.find_element_by_id("pincode")
elem.send_keys(pincode)
time.sleep(1)

elem = driver.find_element_by_id("book")
elem.click()
time.sleep(5)


driver.close()
