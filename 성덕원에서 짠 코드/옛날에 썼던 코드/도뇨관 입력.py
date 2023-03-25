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

driver.find_element("xpath", '//*[@id="vipsFrm"]/div/section[1]/div/ul/li[2]/div/div/button').click()

driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[-1])

is_xpath_exist(driver, '//*[@id="mainmenu"]/ul/li[4]/ul/li[4]/a')
driver.find_element('xpath', '//*[@id="mainmenu"]/ul/li[4]/ul/li[4]/a').click()

is_xpath_exist(driver, '//*[@id="gnb"]/ul/li[3]')
driver.find_element('xpath', '//*[@id="gnb"]/ul/li[3]').click()

is_xpath_exist(driver, '//*[@id="gnb"]/ul/li[3]/ul/li[2]/a')
driver.find_element('xpath', '//*[@id="gnb"]/ul/li[3]/ul/li[2]/a').click()

driver.switch_to.window(driver.window_handles[-1])

driver.find_element('xpath', '//*[@id="start_dt"]').click()

#년도
Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]')).select_by_value("2022")

#월
Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_value("0")

#날짜
driver.find_element(By.LINK_TEXT, "1").click()

#driver.find_element("xpath", '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[3]').click()
driver.find_element("xpath", '//*[@id="content"]/div/div[2]/div[1]/span[1]/span[1]/span/span[2]').click()
driver.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys("김귀례" + Keys.ENTER)
driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[1]/ul/li[5]/a/span').click()

li_1 = [3,7,12,15,19,23]
li_2 = [1,7,17]

while 1:
    if driver.find_element('xpath', '//*[@id="start_dt"]').get_attribute('value') == '2022-10-01':
        break
    if driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/span[2]').text != '':
        # 전체 삭제
        driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/ul/li[4]/a').click()
        '//*[@id="content"]/div/div[3]/div[4]/div/div/ul/li[4]/a'
        result5 = driver.switch_to.alert
        result5.accept()
        driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/div/a[2]/span').click()
    else:
        #전체 삭제
        driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/ul/li[4]/a').click()
        '//*[@id="content"]/div/div[3]/div[4]/div/div/ul/li[4]/a'
        result5 = driver.switch_to.alert
        result5.accept()

        for i in range(3):
            driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[5]/div/div[1]/div/div/div[{}]'.format(i+1)).click()

        for i in range(len(li_1)):
            ur_min = random.randint(1, 5)
            water = 50 * random.randint(4, 6)
            """
            if i == 2:
                ur_min = random.randint(1,3)
            elif i == 4:
                ur_min = random.randint(9,11)
            """
            # 시간
            Select(driver.find_element('xpath', '// *[ @ id = "urine_h"]')).select_by_index(li_1[i])
            # 분
            Select(driver.find_element('xpath', '// *[ @ id = "urine_m"]')).select_by_index(ur_min)
            driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/p/input').clear()
            driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/p/input').send_keys(
                str(water) + Keys.ENTER)

            driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/ul/li[1]/a').click()

        driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/p/input').clear()
        driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/p/input').send_keys()

        driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/div/a[2]/span').click()
"""
while 1:
    if driver.find_element('xpath', '//*[@id="start_dt"]').get_attribute('value') == '2022-09-27':
        break
    #전체 삭제
    driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/ul/li[4]/a').click()
    '//*[@id="content"]/div/div[3]/div[4]/div/div/ul/li[4]/a'
    result5 = driver.switch_to.alert
    result5.accept()

    for i in range(3):
        driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[5]/div/div[1]/div/div/div[{}]'.format(i+1)).click()

    for i in range(len(li_2)):
        ur_min = random.randint(1, 5)
        water = 50 * random.randint(4, 6)
        if driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/span[2]').text != '':
            water = 3000
        # 시간
        Select(driver.find_element('xpath', '// *[ @ id = "urine_h"]')).select_by_index(li_2[i])
        # 분
        Select(driver.find_element('xpath', '// *[ @ id = "urine_m"]')).select_by_index(ur_min)
        driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/p/input').clear()
        driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/p/input').send_keys(
            str(water) + Keys.ENTER)

        driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/ul/li[1]/a').click()

    driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/p/input').clear()
    driver.find_element('xpath', '//*[@id="content"]/div/div[3]/div[4]/div/div/p/input').send_keys()

    driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div[1]/div/a[2]/span').click()
"""
