from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import urllib.request as ureq
x=input("Enter term to be searched. In case of multiple words use + to concatenate them(Eg table+top):")
ser=Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver=webdriver.Chrome(service=ser)
driver.get('https://www.google.com/search?q='+x)
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element(By.LINK_TEXT, 'Images').click()
image_list=driver.find_elements(By.TAG_NAME,'img')
j=1
for i in image_list:
    src=i.get_attribute('src')
    try:
        if(src):
            png = re.search('png', src)
            svg = re.search('svg', src)
            if(png):
                pass
            elif(svg):
                pass
            else:
                ureq.urlretrieve(str(src), 'C:/Users/1001t/Downloads/Images/' + x + str(j) + ".jpg")
                j = j + 1
    except Exception as e:
        print(e)
        continue

sleep(5)
driver.close()
