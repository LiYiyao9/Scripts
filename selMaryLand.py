import time
from time import sleep
import os.path
from random import randint
from selenium import webdriver


url = "http://www.city-data.com/so/Maryland.html"
links = []
file = open("name_maryland.txt","w",encoding='utf-8')
xPath_name = '//*[@id="{}"]'

driver = webdriver.Chrome(r'path to directory of chrome driver')
driver.implicitly_wait(120)
driver.get(url)
driver.maximize_window()
try:
    elements = driver.find_elements(By.TAG_NAME,"a")
    for element in elements:
        element_link = element.get_attribute('href')
        if element_link is not None:
            if "http://www.city-data.com/so/so-" in element_link:
                links.append(element_link)
    for link in links:
        driver.get(link)
        numbers = driver.find_elements(By.TAG_NAME,"span")
        for number in numbers:
            number_id = number.get_attribute('id')
            if "sn" in number_id:
                name = driver.find_element_by_xpath(xPath_name.format(number_id))
                if "Aliases" in name.text:
                    cleaned_names = name.text.replace("(Aliases: ","").strip(")").replace('\n',";").split(";")
                    for i in range(0,len(cleaned_names)):
                        file.write(cleaned_names[i] + '\n')
                else:
                    file.write(name.text + '\n')
    sleep(randint(2,3))
    file.close()
except Exception as e:
    print(e)
finally:
    driver.quit()
