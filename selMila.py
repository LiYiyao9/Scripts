import time
from time import sleep
import os.path
from random import randint
from bs4 import BeautifulSoup
from mtranslate import translate
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# example of input keys

url = "http://www.inmatesearch.mkesheriff.org/"

file=open("Milwaukee_inmates.txt","w",encoding='utf-8')

xPath = '/html/body/form/center/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr[1]/td/div/table/tbody/tr[1]/td[1]/table/tbody[2]/tr/td/div[2]/table/tbody/tr/td[21]'

driver = webdriver.Chrome(r'path to directory of chrome driver')
driver.implicitly_wait(120)
driver.get(url)
driver.maximize_window()

try:
    for i in range(97,123):
        driver.implicitly_wait(600)
        element = driver.find_element_by_xpath('//*[@id="_ctl0_CpnlMain_ctrlUsrSrchTools_txtLastName"]')
        element.send_keys(chr(i))
        sleep(randint(2,3))
        driver.find_element_by_xpath('//*[@id="_ctl0_CpnlMain_ctrlUsrSrchTools_cmdSearch"]').click()
        sleep(randint(2,3))
        contents = driver.find_elements_by_xpath(xPath)
        for content in contents:
            driver.execute_script("arguments[0].scrollIntoView();", content)
            file.write(content.text + '\n')
        sleep(randint(2,3))
        element_remove = driver.find_element_by_xpath('//*[@id="_ctl0_CpnlMain_ctrlUsrSrchTools_txtLastName"]')
        element_remove.send_keys(Keys.BACKSPACE)
    file.close()
except Exception as e:
    print(e)
finally:
    driver.quit()