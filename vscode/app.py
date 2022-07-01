import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import copy
import pyperclip
import pyautogui





driver = webdriver.Chrome() # Driver가 있는 path를 넣어 줄 수 있음

time.sleep(2)

driver.get("https://app.tosspayments.com/")

time.sleep(3 * random.random())


elems = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/section/div[3]/div[3]/table/tbody')

n = 0
li = []
l = []

for i in elems.find_elements_by_class_name('text--left'):
    if n % 10 == 0:
#         print("날짜 : ",i.text)
        l.append(i.text)
    elif n % 10 == 2: # 결제 완료 여부
        l.append(i.text)
    elif n % 10 == 3:
#         print("컨텐츠 : ",i.text)
        l.append(i.text)
    elif n % 10 == 5:
#         print("이름 : ",i.text)
        l.append(i.text)
    elif n % 10 == 7:
#         print("번호 : ",i.text)
        l.append(i.text)
        li.append(l)
        l = []
    n += 1
