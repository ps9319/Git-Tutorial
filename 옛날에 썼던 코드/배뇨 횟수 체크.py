import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import warnings
import random

warnings.filterwarnings("ignore")


def is_xpath_exist(dr, xpath):
    try:
        # xpath가 로딩될 때 까지 10초 대기
        element = WebDriverWait(dr, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except:
        return 0


def six_to_ten(min, op):
    if op == 1:
        put_hour = min // 60
        if put_hour < 10:
            put_hour = '0' + str(put_hour)
        elif put_hour == 11 or put_hour ==12 or put_hour==10:
            put_hour = str(put_hour)
        else:
            put_hour = str(put_hour) + '(오후' + str(put_hour-12) + '시)'
        return put_hour

    elif op == 2:
        put_min = min % 60
        if put_min < 10:
            put_min = '0' + str(put_min)
        else:
            put_min = str(put_min)
        return put_min


def choice_name(time, name_list):
    if time < 510:
        return name_list[0]
    elif time < 1080:
        return name_list[1]
    else:
        return name_list[2]
"""
real_name = input("이름 입력 :")
year = input("년도 입력 : ")
month = str(int(input("월 입력 : ")) - 1)
date = input("일 입력 : ")
ESC_date = input("끝 날짜 (2022-01-01)")
"""

year = '2022'
month = '6'
date = '1'
ESC_date = '2022-07-31'

driver = webdriver.Chrome()
url = 'http://www.lcms.or.kr/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

loginID_1 = "sdwon"
loginID_2 = "fks6628"
loginID_3 = "fks1114"

# 로그인
is_xpath_exist(driver, '//*[@id="f_code"]')

driver.find_element("xpath", '//*[@id="f_code"]').send_keys(loginID_1)
driver.find_element("xpath", '//*[@id="id"]').send_keys(loginID_2)
driver.find_element("xpath", '//*[@id="pwd"]').send_keys(loginID_3)

driver.find_element("xpath", '//*[@id="content"]/section[2]/div[1]/div[2]/div/div[3]/a[1]').click()

driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[-1])

is_xpath_exist(driver, '//*[@id="mainmenu"]/ul/li[4]/ul/li[4]/a')
driver.find_element('xpath', '//*[@id="mainmenu"]/ul/li[4]/ul/li[4]/a').click()

is_xpath_exist(driver, '//*[@id="gnb"]/ul/li[3]')
driver.find_element('xpath', '//*[@id="gnb"]/ul/li[3]').click()

driver.find_element('xpath', '//*[@id="gnb"]/ul/li[3]/ul/li[2]/a').click()

driver.switch_to.window(driver.window_handles[-1])

is_xpath_exist(driver, '//*[@id="start_dt"]')
driver.find_element('xpath', '//*[@id="start_dt"]').click()

#년도 입력
Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]')).select_by_value(year)
#월 입력 월-1
Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_value(month)
#날짜 입력
driver.find_element(By.LINK_TEXT, date).click()

#driver.find_element("xpath", '//*[@id="content"]/div/div[2]/div[1]/span[1]/span[1]/span/span[2]').click()
#driver.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys(real_name + Keys.ENTER)


name_list = ['최정자','탁봉순','하태순','한순임','허경임','허야무']
for i in range(len(name_list)):
    is_xpath_exist(driver, '//*[@id="start_dt"]')
    driver.find_element('xpath', '//*[@id="start_dt"]').click()

    # 년도 입력
    Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]')).select_by_value(year)
    # 월 입력 월-1
    Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_value(month)
    # 날짜 입력
    driver.find_element(By.LINK_TEXT, date).click()

    driver.find_element("xpath", '//*[@id="content"]/div/div[2]/div[1]/span[1]/span[1]/span/span[2]').click()
    driver.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys(name_list[i] + Keys.ENTER)

    while 1:
        is_xpath_exist(driver, '//*[@id="start_dt"]')
        now_date = driver.find_element('xpath', '//*[@id="start_dt"]').get_attribute("value")

        is_xpath_exist(driver, '//*[@id="content"]/div/div[3]/div[5]/div/div/p/input')
        pee_num = int(
            driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[5]/div/div/p/input').get_attribute("value"))

        if pee_num <= 8:
            print(name_list[i] + ' ' + now_date)

        # 다음 클릭
        driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/div/a[2]/span').click()

        if now_date == ESC_date:
            break








