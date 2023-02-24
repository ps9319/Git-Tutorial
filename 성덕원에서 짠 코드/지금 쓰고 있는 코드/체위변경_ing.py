# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import warnings
import get_name_list

warnings.filterwarnings("ignore")


def is_xpath_exist(dr, xpath):
    try:
        # xpath가 로딩될 때 까지 10초 대기
        element = WebDriverWait(dr, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except:
        return 0


# name = input("이름을 입력하세요 : ")
name = '양소례'
# year, month, date = map(int, input("년도와 월을 입력해주세요. ex)2023 2 24").split())
year, month, date = 2022, 6, 29

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
driver.find_element('xpath', '//*[@id="f_code"]').send_keys(loginID_1)
driver.find_element('xpath', '//*[@id="id"]').send_keys(loginID_2)
driver.find_element('xpath', '//*[@id="pwd"]').send_keys(loginID_3)
driver.find_element('xpath', '//*[@id="vipsFrm"]/div/section[1]/div/ul/li[2]/div/div/button').click()

driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[-1])

# 기록지 클릭
is_xpath_exist(driver, '//*[@id="mainmenu"]/ul/li[4]/ul/li[7]/a')
driver.find_element('xpath', '//*[@id="mainmenu"]/ul/li[4]/ul/li[7]/a').click()
# 체위 변경 클릭
is_xpath_exist(driver, '//*[@id="content"]/div/div[1]/div[2]/div[2]/div[2]/label')
driver.find_element('xpath', '//*[@id="content"]/div/div[1]/div[2]/div[2]/div[2]/label').click()
# 입소자 명단 클릭
driver.find_element('xpath', '//*[@id="content"]/div/div[1]/div[2]/div[2]/span/span[1]/span/span[2]').click()
driver.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys(name + Keys.ENTER)
# 날짜 입력
driver.find_element('xpath', '//*[@id="month_start_dt"]').click()
driver.find_element(By.CLASS_NAME, 'mtz-monthpicker').click()
Select(driver.find_element(By.CLASS_NAME, 'mtz-monthpicker-year')).select_by_value(str(year))

if month % 3 == 0:
    tr = month // 3
    td = 3
else:
    tr = month // 3 + 1
    td = month % 3
driver.find_element('xpath', '/html/body/div[4]/table/tbody/tr[{}]/td[{}]'.format(tr, td)).click()
driver.find_element('xpath', '/html/body/div[3]/form/section[1]/div/div[2]/div/table/tbody/tr[1]/td[{}]'.format(date + 1)).click()
# 화면 전환
driver.switch_to.window(driver.window_handles[-1])


# 전체삭제
driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[3]/div[4]/div/div/ul/li[2]/a').click()
window_pop = Alert(driver)
window_pop.accept()
