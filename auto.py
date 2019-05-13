from selenium import webdriver

import time

with open('account.info', 'r') as f:
    username = f.readline().strip('\n')
    password = f.readline()

chrome_path='./chromedriver-mac'
browser = webdriver.Chrome(chrome_path)
browser.get('http://www.1point3acres.com/bbs/')
browser.find_element_by_id("ls_username").send_keys(username)
browser.find_element_by_id("ls_password").send_keys(password)
time.sleep(5)

try:
    browser.find_element_by_css_selector("button.pn.vm").click()
    time.sleep(5)
    browser.find_element_by_xpath("//div[@id='um']/p/a[4]/font").click()
    time.sleep(3)
    browser.find_element_by_css_selector("#fd > center > img").click()
    time.sleep(3)
    browser.find_element_by_id("todaysay").send_keys("check in")
    time.sleep(3)
    browser.find_element_by_css_selector("button.pn.pnc").click()
    browser.quit()
except:
    browser.quit()