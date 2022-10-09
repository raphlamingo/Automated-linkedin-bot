import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
chrome_drive='C:\developer\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_drive)
browser.get('https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom')
linkedin=browser.find_element(by=By.CLASS_NAME, value='nav__button-secondary')
linkedin.click()
time.sleep(5)
user= browser.find_element(by=By.ID,value='username')
user.send_keys('igwerapheal2@gmail.com')
password= browser.find_element(by=By.ID,value='password')
password.send_keys('Hallelcollege1')
button= browser.find_element(by=By.CSS_SELECTOR,value='.login__form_action_container')
time.sleep(3)
button.click()
apply=browser.find_element(by=By.CSS_SELECTOR,value='li a')
apply.click()
save=browser.find_element(by=By.CLASS_NAME,value='jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary')
save.click()