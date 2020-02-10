import time
from time import sleep
import csv
import os.path
import pandas as pd
from random import randint
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

# China tatler scrapping with auto scrolling

url="http://www.shangliutatler.com/tatler-list/300list"

xpath_links = '/html/body/div[1]/div[6]/div/div/div[1]/div/div/div/a'

links = []
temp = []
final = []
driver = webdriver.Chrome(r'path of directory with chrome driver')
driver.implicitly_wait(300)
driver.get(url)
driver.maximize_window()

try:
    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            contents = driver.find_elements_by_xpath(xpath_links)
            for content in contents:
                links.append(content.get_attribute('href'))
            break
        last_height = new_height
    for link in links:
        link_name = link.replace("http://www.shangliutatler.com/tatler-list/300list/","")
        if "-2018" in link_name:
            link_name_ph_1=link_name.replace("-2018","")
            temp.append(link_name_ph_1.replace("-"," "))
        elif"%20" in link_name:
            temp.append(link_name.replace("%20"," "))
        else:
            temp.append(link_name)
    df = pd.DataFrame(temp)
    df.to_csv('cn_name.csv',encoding='utf-8-sig')
except Exception as e:
    print(e)
finally:
    driver.quit()