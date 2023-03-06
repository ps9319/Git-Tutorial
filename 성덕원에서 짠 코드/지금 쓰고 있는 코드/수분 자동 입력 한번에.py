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


def put_auto(driver, name):
    # 날짜 클릭
    is_xpath_exist(driver, '//*[@id="start_dt"]')
    driver.find_element('xpath', '//*[@id="start_dt"]').click()
    # 월
    Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_value(str(int(month)-1))

    # 날짜
    driver.find_element(By.LINK_TEXT, str(date)).click()

    # 입소자 명단 클릭
    is_xpath_exist(driver, '//*[@id="content"]/div/div[1]/div[2]/div[2]/div/span/span[1]/span/span[2]')
    driver.find_element('xpath', '//*[@id="content"]/div/div[1]/div[2]/div[2]/div/span/span[1]/span/span[2]').click()

    # 이름 입력
    is_xpath_exist(driver, '/html/body/span/span/span[1]/input')
    driver.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys(name + Keys.ENTER)

    # 현재 날짜 존재 확인
    result = is_xpath_exist(driver, '//*[@id="content"]/div/div[2]/section[1]/table/tbody/tr/td[8]/div/table/thead/tr/td[1]')

    # 날짜 클릭
    if result != 0:
        driver.find_element('xpath',
        '//*[@id="content"]/div/div[2]/section[1]/table/tbody/tr/td[8]/div/table/thead/tr/td[1]').click()
        if driver.find_element('xpath', '/html/body/div[3]/form/section/div/div[1]/div[2]/div[2]/span[2]').is_displayed():
            driver.back()
        else:
            # 시간 선택
            hour = {"1": 7, "3": 9, "5": 11, "7": 13, "9": 15, "11": 18, "13": 20}
            minute = {"2": random.randint(7, 9), "4": random.randint(5, 7), "6": random.randint(1, 3),
            "8": random.randint(5, 7), "10": random.randint(10, 12), "12": random.randint(5, 7),
            "14": random.randint(5, 7)}

            # 분
            is_xpath_exist(driver, '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/select[1]')
            for i in range(0, 7):
                Select(driver.find_element('xpath',
                '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/select[{}]'.format(i * 2 + 1))).select_by_index(
                hour.get(str(i * 2 + 1)))
            # 분 선택
            for i in range(1, 8):
                Select(driver.find_element('xpath',
                '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/select[{}]'.format(i * 2))).select_by_index(
                minute.get(str(i * 2)))

            # 08시부터 17시까지
            for i in range(2, 7):
                driver.find_element('xpath',
                '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/input[{}]'.format(i)).clear()

                driver.find_element('xpath',
                '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/input[{}]'.format(i)).send_keys(
                int(10 * random.randint(16, 18)))

            # 06시와 19시
            for i in range(2):
                driver.find_element('xpath',
                '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/input[{}]'.format(6 * i + 1)).clear()

                driver.find_element('xpath',
                '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/input[{}]'.format(6 * i + 1)).send_keys(
                int(10 * random.randint(14, 15)))

            for i in range(4):
                Select(driver.find_element('xpath',
                    '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/select[{}]'.format(i + 15))).select_by_index(0)

            for i in range(2):
                driver.find_element('xpath', '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/input[{}]'.format(i + 8)).clear()
                driver.find_element('xpath', '/html/body/div[3]/form/section/div/div[2]/div/table/tbody/tr[20]/td[3]/input[{}]'.format(i + 8)).send_keys('0')

            # 저장
            driver.find_element('xpath', '/html/body/div[3]/form/section/div/div[1]/div[2]/div[3]/button[4]').send_keys(Keys.ENTER)
            window_pop = Alert(driver)
            window_pop.accept()
            is_xpath_exist(driver, '/html/body/div[3]/form/section/div/div[1]/div[2]/div[3]/button[4]')

            #시험
            driver.back()
            driver.back()
    elif is_xpath_exist(driver, '//*[@id="select2-seq_value-results"]/li') != 0:
        driver.find_element('xpath',
            '/html/body/span/span/span[1]/input').clear()
        driver.find_element('xpath',
            '//*[@id="content"]/div/div[1]/div[2]/div[2]/div/span/span[1]/span/span[2]').click()
    else:
        driver.back()




month = input("월을 입력하세요 : ")
date = int(input("시작 날짜를 입력하세요 : "))
op = int(input("끝 날짜를 입력하세요 : "))
op = op - date + 1

name_list = get_name_list.get_name()
#name_list = ['강복순', '강순남', '강재현', '김갑순', '김귀임', '김남석', '김단례', '김도순', '김분임', '김성순', '김성임', '김순화', '김애덕', '김춘선', '김춘자', '박당녀', '박형봉', '서옥순', '송영자', '심삼남', '양소례', '우복인', '유복', '윤점례', '이상수', '이선미', '이얌순', '이양님', '이정애', '임계순', '임순덕', '전신자', '전점례', '정귀모', '정중헌', '정해님', '조대섭', '주순남', '주정애', '진병금', '진정님', '최순옥', '최영애', '탁봉순', '하태순', '한순임', '허경임', '허야무']

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
is_xpath_exist(driver, '//*[@id="mainmenu"]/ul/li[3]/ul/li[1]/a')
driver.find_element('xpath', '//*[@id="mainmenu"]/ul/li[3]/ul/li[1]/a').click()

for j in range(op):
    start = time.time()
    for i in range(len(name_list)):
        put_auto(driver, name_list[i])
    date += 1
    print("날짜", date, "시간 :", time.time() - start, "초 걸림")
