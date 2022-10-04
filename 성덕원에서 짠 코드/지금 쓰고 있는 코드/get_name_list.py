from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def is_xpath_exist(dr, xpath):
    try:
        # xpath가 로딩될 때 까지 10초 대기
        element = WebDriverWait(dr, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except:
        return 0


def get_name():
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
    driver.find_element_by_xpath('//*[@id="f_code"]').send_keys(loginID_1)
    driver.find_element_by_xpath('//*[@id="id"]').send_keys(loginID_2)
    driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(loginID_3)
    driver.find_element_by_xpath('//*[@id="content"]/section[2]/div[1]/div[2]/div/div[3]/a[1]').click()

    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

    driver.find_element_by_xpath('//*[@id="mainmenu"]/ul/li[1]/ul/li[1]/a').click()

    try:
        tmp = 1
        name_list = []
        while 1:
            name_list.append(driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[5]'.format(tmp)).text)
            tmp += 1
    except:
        pass

    return name_list
