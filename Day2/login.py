#Python program to login to flipkart account using selenium webdriver 


from selenium import webdriver

from selenium.webdriver.chrome.service import Service
path = Service("C:\\Users\\ELCOT\\Desktop\\python\\webdrivers\\chromedriver.exe")

from getpass import getpass
mail = input('Enter your flipkart ID ')
pwd = getpass('Enter your password')

browser = webdriver.Chrome(service=path)
browser.maximize_window()

browser.get('https://www.flipkart.com/')

from selenium.webdriver.common.by import By

browser.find_element(By.XPATH, '//input[@class="_2IX_2- VJZDxU"]').send_keys(mail)
browser.find_element(By.XPATH, '//input[@type="password"]').send_keys(pwd)
browser.find_element(By.CSS_SELECTOR, 'button[class="_2KpZ6l _2HKlqd _3AWRsL"]').click()