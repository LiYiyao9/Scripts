import requests
import urllib.request
import time
from time import sleep
import os.path
from random import randint
from selenium import webdriver

# pdf download exmaple

url = "https://tncourts.gov/courts/court-appeals/opinions"
header = "https://tncourts.gov/courts/court-appeals/opinions?page={}" 

directory = "Tncourt_Pdf"
directory_text = "Tncourt_Text"

if not os.path.exists( directory) and not os.path.exists(directory_text):
    os.makedirs(directory)
    os.makedirs(directory_text)

max_page = 0
count = 0
links = []

def checkUrl(link):
    try:
        website = urllib.request.urlopen(link)
        website.close()
        return True
    except:
        return False


driver = webdriver.Chrome(r'path of directory with chrome driver')
driver.implicitly_wait(300)
driver.get(url)
driver.maximize_window()

try:
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div[3]/ul/li[12]/a').click()
    lastPage = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div/div/div[3]/ul/li[12]')
    max_page = int(lastPage.text)

    first_page_contents = driver.find_elements(By.TAG_NAME,"a")
    for page_content in first_page_contents:
        page_url = page_content.get_attribute('href')
        if page_url is not None and "pdf" in page_url:
            links.append(page_url)
    
    for i in range(1,max_page):
        driver.get(header.format(i))
        content_urls = driver.find_elements(By.TAG_NAME,"a")
        for content_url in content_urls:
            artcle_url = content_url.get_attribute('href')
            if artcle_url is not None and "pdf" in artcle_url:
                links.append(artcle_url)
    
    for link in links:
        file_name = 'file{}.pdf'.format(count)
        folder = os.path.join(directory, file_name) 
        if checkUrl(link):
            urllib.request.urlretrieve(link,folder)
            count+= 1
except Exception as e:
    print(e)
finally:
    driver.quit()
