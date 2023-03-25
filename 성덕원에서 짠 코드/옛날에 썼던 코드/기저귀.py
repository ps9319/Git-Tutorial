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

real_name = input("이름 입력 :")
year = input("년도 입력 : ")
month = str(int(input("월 입력 : ")) - 1)
date = input("일 입력 : ")
ESC_date = input("끝 날짜 (2022-01-01)")


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

driver.find_element("xpath", '//*[@id="content"]/div/div[2]/div[1]/span[1]/span[1]/span/span[2]').click()
driver.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys(real_name + Keys.ENTER)

tmp = 0
while 1:
    is_xpath_exist(driver, '//*[@id="start_dt"]')
    now_date = driver.find_element('xpath', '//*[@id="start_dt"]').get_attribute("value")
    if driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/span[2]').text != '':
        name_exist = "입원 또는 외래"
    else:
        is_xpath_exist(driver, '//*[@id="content"]/div/div[3]/div[5]/div/table/tbody/tr[1]/td[6]')
        name_exist = driver.find_element('xpath',
                                         '//*[@id="content"]/div/div[3]/div[5]/div/table/tbody/tr[1]/td[6]').text

    if driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/span[2]').text == '' and (name_exist != ' '):
        pee_num = int(
            driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[5]/div/div/p/input').get_attribute("value"))

        pee_list = [0 for i in range(pee_num)]
        if driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[5]/div/table/tbody/tr[1]/td[3]').text != '기저귀':
            print(now_date + " 기저귀 아님")
            break
        for i in range(int(pee_num)):
            pee_list[i] = driver.find_element('xpath',
                                              '//*[@id="content"]/div/div[3]/div[5]/div/table/tbody/tr[{}]/td[1]'.format(
                                                  i + 1)).text

        for i in range(int(pee_num)):
            pee_list[i] = int(pee_list[i][0]) * 600 + int(pee_list[i][1]) * 60 + int(pee_list[i][5]) * 10 + int(
                pee_list[i][6])

        # put list 몇번째인지
        put_list_num = []
        # 넣어야할 시간
        put_list = []

        for i in range(int(pee_num) - 1):
            if pee_list[i + 1] - pee_list[i] >= 180:
                put_list_num.append(i)

        # 넣어야할 시간 만들기
        for i in range(len(put_list_num)):
            extra = (pee_list[put_list_num[i] + 1] - pee_list[put_list_num[i]]) * 0.5
            extra = int((extra // 10) * 10)
            put_list.append(pee_list[put_list_num[i]] + extra)

        put_ten_thirty = 0
        for i in range(int(pee_num)):
            if pee_list[i] > 1320:
                put_ten_thirty += 1
            else:
                pass
        if put_ten_thirty == 0:
            put_list.append(1350)

        name_list = []
        name_list.append(
            driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[5]/div/table/tbody/tr[1]/td[6]').text)
        for i in range(pee_num):
            for j in range(len(name_list)):
                if driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[5]/div/table/tbody/tr[{}]/td[6]'.format(
                        i + 1)).text not in name_list:
                    name_list.append(driver.find_element('xpath',
                                                         '//*[@id="content"]/div/div[3]/div[5]/div/table/tbody/tr[{}]/td[6]'.format(
                                                             i + 1)).text)
        if len(name_list) != 3:
            print(now_date + " 이름 세 명 아님")
            driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/div/a[2]/span').click()
            continue
        for i in range(len(put_list)):
            put_hour = six_to_ten(put_list[i], 1)
            put_min = six_to_ten(put_list[i], 2)
            # 기저귀확인 클릭
            driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div[1]/ul/li[3]/a/em').click()
            # 시간 클릭
            driver.find_element('xpath', '//*[@id="rest_hh"]').click()
            # driver.find_element('xpath', '//*[@id="test3"]/div[2]/div/div/div[2]/div/ul/li[1]/a/span').click()
            driver.find_element(By.LINK_TEXT, put_hour).click()
            # 분 클릭
            driver.find_element('xpath', '//*[@id="rest_mm"]').click()
            # driver.find_element('xpath', '//*[@id="test4"]/div[2]/div/div/div[2]/div[2]/ul/li[1]/a/span').click()
            driver.find_element(By.LINK_TEXT, put_min).click()
            # 이름 입력
            driver.find_element('xpath', '//*[@id="rest_nappy_stff_nm"]').click()
            driver.find_element('xpath', '//*[@id="test5"]/div[2]/div/div/div[2]/div[1]/a').click()
            driver.find_element('xpath', '//*[@id="rest_nappy_stff_nm"]').send_keys(
                choice_name(put_list[i], name_list) + Keys.ENTER)
            # 저장
            driver.find_element('xpath', '//*[@id="rest_save"]').click()
    elif name_exist == ' ':
        print(now_date + " 이름 입력 안 함")
    else:
        print(now_date + " " + driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/span[2]').text)
    tmp += 1


    # 다음 클릭
    driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/div/a[2]/span').click()

    if now_date == ESC_date:
        break






