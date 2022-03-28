#Python program to open a browser

from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:\\Users\\ELCOT\\Desktop\\python\\webdrivers\\chromedriver.exe")

browser.get('https://www.youtube.com/watch?v=jmwU1iAC-IE')
print(browser.title)
browser.fullscreen_window()
