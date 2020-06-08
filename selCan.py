import xml.etree.ElementTree as ET
import time
from time import sleep
from random import randint
from selenium import webdriver

#example of xml tree 

url="https://www.international.gc.ca/world-monde/assets/office_docs/international_relations-relations_internationales/sanctions/sema-lmes.xml"
companies_text = open("Canada_companies_DFATD.txt","w",encoding = 'utf-8')
names_text = open("Canada_names_DFATD.txt","w",encoding = 'utf-8')

driver = webdriver.Chrome(r'path of directory with chrome driver')
driver.implicitly_wait(120)
driver.get(url)
driver.maximize_window()

try:
    root = ET.fromstring(driver.page_source)
    for ent in root.iter('record'):
        inc = ent.find('Entity')
        lastName = ent.find('LastName')
        givenName = ent.find('GivenName')
        if inc is not None:
            companies_text.write(inc.text + '\n')
        else:
            if givenName is not None and lastName is not None:
                names_text.write(givenName.text + " " + lastName.text + '\n')
    companies_text.close()
    names_text.close()

except Exception as e:
    print(e)
finally:
    driver.quit()
