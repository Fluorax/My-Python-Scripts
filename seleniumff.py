#!/usr/bin/env python
#code to initiallize FF 80 /w Gecko 0.27 on Manjaro. Be sure to set PATH for Gecko
import requests, time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def terminate():
    driver.quit() #terminate driver
    time.sleep(1200) #polls every 20 minutes

while True:
    binary = FirefoxBinary('/usr/lib/firefox/firefox')
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', firefox_binary=binary)
    wait = WebDriverWait(driver, 10)

    #opens website
    driver.minimize_window()
    driver.get('login_page') #website_login_page

    #Inputs username & password - check field ids /w inspect element
    userElem = driver.find_element_by_id('userName') #name id
    userElem.send_keys('username') #username
    passwordElem = wait.until(EC.presence_of_element_located((By.ID, "pwd")))
    #passwordElem = driver.find_element_by_id('pwd') #name id
    passwordElem.send_keys('password')  #password
    nextElem = driver.find_element_by_id('submit1') #name id
    nextElem.click()

    #navigate to results
    driver.get('scrape_target') #page to scrape data from

    #Locate and get desired values
    SemesterElem = driver.find_element_by_css_selector('') #scrape specific css element from table
    GradeElem = driver.find_element_by_css_selector('') #scrape specific css element from table
    
    #loop - post only if semester!=old
    if SemesterElem.text!=str('ΦΕΒΡ  2019-2020'): 
        results = (str("Βαθμός:" + " " + GradeElem.text + "   " + "Εξεταστική:" + " " + SemesterElem.text))
        requests.get("telegram_bot_API".format(results)) #telegram_bot_API

    terminate()
        
