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
from tkinter import *
import tkinter as tk
is_ID, is_DATE = False, False
def enable_execute_button():
    if is_ID and is_DATE:
        execute_button['state'] = tk.NORMAL
def put_ID():
    global loginID_2, loginID_3, is_ID
    loginID_2 = loginID_input2.get()
    loginID_3 = loginID_input3.get()
    is_ID = True
    enable_execute_button()
def put_DATE():
    global month, start_date, end_date, is_DATE
    month = month_input.get()
    start_date = int(start_date_input.get())
    end_date = int(end_date_input.get())
    end_date = end_date - start_date + 1
    is_DATE = True
    enable_execute_button()
    return
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

    # 로그인
    is_xpath_exist(driver, '//*[@id="f_code"]')
    driver.find_element('xpath', '//*[@id="f_code"]').send_keys(loginID_1)
    driver.find_element('xpath', '//*[@id="id"]').send_keys(loginID_2)
    driver.find_element('xpath', '//*[@id="pwd"]').send_keys(loginID_3)
    driver.find_element('xpath', '//*[@id="vipsFrm"]/div/section[1]/div/ul/li[2]/div/div/button').click()

    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

    driver.find_element('xpath', '//*[@id="mainmenu"]/ul/li[1]/ul/li[1]/a').click()

    try:
        tmp = 1
        name_list = []
        while 1:
            name_list.append(driver.find_element('xpath', '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[5]'.format(tmp)).text)
            tmp += 1
    except:
        pass

    return name_list
def put_auto(driver, name):
    global start_date
    # 날짜 클릭
    is_xpath_exist(driver, '//*[@id="start_dt"]')
    driver.find_element('xpath', '//*[@id="start_dt"]').click()
    # 월
    Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_value(str(int(month)-1))

    # 날짜
    driver.find_element(By.LINK_TEXT, str(start_date)).click()

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


window = tk.Tk()
window.title("수분 자동 입력기")
window.geometry("325x110-700+400")
#window.resizable(False, False)

loginID_1 = "sdwon"
loginID_2 = StringVar()
loginID_3 = StringVar()
month = StringVar()
start_date = StringVar()
end_date = StringVar()

loginID_label2 = Label(window, text="아이디    : ", anchor= 'w', width=10)
loginID_label2.grid(row=0, column =0)

loginID_label3 = Label(window, text="비밀번호 : ", anchor= 'w',width=10)
loginID_label3.grid(row=1, column =0)

loginID_input2 = tk.Entry(window)
loginID_input2.grid(row=0, column=1, columnspan=4)

loginID_input3 = tk.Entry(window)
loginID_input3.grid(row=1, column=1, columnspan=4)

login_button = tk.Button(window, text="입력", width=5, command=put_ID)
login_button.grid(row=0, column=6, rowspan=2,sticky='w'+'e'+'s'+'n', padx=5)

information_label = Label(window, text="아래에 시작 월과 날짜를 입력해주세요")
information_label.grid(row=2, column=0, columnspan=7)

start_date_label = Label(window, text="시작 날짜 ", anchor= 'w',width=10)
start_date_label.grid(row=3, column=0)

month_input = tk.Entry(window, width= 2)
month_input.grid(row=3, column=1, sticky='w')

month_letter = Label(window, text="월", width=1)
month_letter.grid(row=3, column=2, sticky='w')

start_date_input = tk.Entry(window, width=2)
start_date_input.grid(row=3, column=3, sticky='w')

start_date2_label = Label(window, text="일",width=1)
start_date2_label.grid(row=3, column=4, sticky='w')

end_date_label = Label(window, text=" 끝 날짜 ", anchor='w',width=10)
end_date_label.grid(row=4, column=0)

end_date_input = tk.Entry(window, width=2)
end_date_input.grid(row=4, column=3, sticky='w')

end_date2_label = Label(window, text="일",width=1)
end_date2_label.grid(row=4, column=4, sticky='w')

date_button = tk.Button(window, text= "날짜\n입력", width=5, command=put_DATE)
date_button.grid(row=3, column=6,rowspan=2,sticky='n'+'e'+'w'+'s', padx= 5)

execute_button = tk.Button(window, text= "실행", width=5, state="disabled", command=window.destroy)
execute_button.grid(row=0, column=7,rowspan=5,sticky='n'+'e'+'w'+'s')
execute_button.pack_forget()

window.mainloop()
name_list = get_name()

driver = webdriver.Chrome()
url = 'http://www.lcms.or.kr/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

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

for j in range(end_date):
    start = time.time()
    for i in range(len(name_list)):
        put_auto(driver, name_list[i])
    start_date += 1
    print("날짜", start_date, "시간 :", time.time() - start, "초 걸림")









