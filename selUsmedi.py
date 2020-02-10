import time
from time import sleep
import csv
import os
import glob
from random import randint
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import selenium.common.exceptions as selexcept
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# exmaple of frame

url = "https://oig.hhs.gov/exclusions/exclusions_list.asp"

company_txt = open("Us_medi_companies.txt","w",encoding='utf-8')
names_txt = open("Us_medi_names.txt","w",encoding='utf-8')

csv_xpath = '//*[@id="anch_24"]'

# get file of csv type in selected directory
def getCsv():
    return [f for f in glob.glob(r'path of selected directory that has csv file type')]

options = webdriver.ChromeOptions() 
prefs = {
"download.default_directory": r"path of selected directory to downnload to",
"download.prompt_for_download": False,
"download.directory_upgrade": True
}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(r'path of directory with chrome driver',options=options)
driver.implicitly_wait(120)
driver.get(url)
driver.maximize_window()

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, csv_xpath))).click()
    sleep(randint(180,185))
    csv_file = getCsv()[0]
    file = open(csv_file)
    csv_reader = csv.reader(file,delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
        if row[3] is not "":
            company_txt.write(row[3] + '\n')
        else:
            if row[2] is not "":
                names_txt.write(row[1] +" "+  row[2] + " "+ row[0] + '\n')
            else:
                names_txt.write(row[1] + " " + row[0] +'\n')
    company_txt.close()
    names_txt.close()
    os.remove(csv_file)
except Exception as e:
    print(e)
finally:
    driver.quit()