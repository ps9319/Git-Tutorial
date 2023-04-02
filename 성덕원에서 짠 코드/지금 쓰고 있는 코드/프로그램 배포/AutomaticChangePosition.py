# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import tkinter as tk
from tkinter import *
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
    global name, start_month, start_date, end_month, end_date, is_DATE
    start_month = int(start_month_input.get())
    start_date = int(start_date_input.get())
    end_month = end_month_input.get()
    end_date = end_date_input.get()
    name = name_input.get()

    if len(end_month) == 1:
        end_month = "0" + end_month
    if len(end_date) == 1:
        end_date = "0" + end_date
    end_date = "2023"+"-"+end_month+"-"+end_date

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
def click_button(hour):
# td 3 4 5 == 좌측위 앙아위 우측위, td 7 8 == 침대 휠체어
# tr == 시간
    # 휠체어
    if hour == fixed_time_list[0] or hour == fixed_time_list[2] or hour == fixed_time_list[4]:
        driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[3]/div[5]/div/table/tbody/tr[{}]/td[{}]/span'.format(hour, 8)).click()
    # 침대
    elif hour == fixed_time_list[1] or hour == fixed_time_list[3]:
        driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[3]/div[5]/div/table/tbody/tr[{}]/td[{}]/span'.format(hour, 7)).click()
    else:
        ran_num = random.randint(3, 5)
        num_list = [3, 4, 5]
        driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[3]/div[5]/div/table/tbody/tr[{}]/td[{}]/span'.format(hour, ran_num)).click()
        try:
            if_alert = Alert(driver)
            if_alert.accept()
            num_list.remove(ran_num)
            driver.find_element('xpath','/html/body/form/div[2]/section[1]/div/div[3]/div[5]/div/table/tbody/tr[{}]/td[{}]/span'.format(hour, num_list[random.randint(0, 1)])).click()
        except:
            pass

    return
def in_and_out():
    three = random.choice([True, False])
    twenty = random.choice([True, False])
    int_list = [6, 8, 10, 15, 17, 23]
    if three:
        result_list.remove(3)
        result_list.append(4)
        result_list.append(2)
    if twenty:
        result_list.remove(20)
        result_list.append(21)
        result_list.append(19)
    for num in int_list:
        if random.choice([True, False]):
            result_list.append(num)
    result_list.sort()
    return
window = tk.Tk()
window.title("수분 자동 입력기")
window.geometry("-700+400")
window.resizable(False, False)

loginID_1 = "sdwon"
loginID_2 = StringVar()
loginID_3 = StringVar()
name = StringVar()
start_month = StringVar()
start_date = StringVar()

end_month = StringVar()
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

information_label = Label(window, text="아래에 이름,시작 월,끝 날짜를 입력해주세요")
information_label.grid(row=2, column=0, columnspan=7)

name_label = Label(window, text="이름")
name_label.grid(row=3, column=0)

name_input = tk.Entry(window)
name_input.grid(row=3, column=1, columnspan=4)

start_date_label = Label(window, text="시작 날짜 ", anchor= 'w',width=10)
start_date_label.grid(row=4, column=0)

start_month_input = tk.Entry(window, width= 2)
start_month_input.grid(row=4, column=1, sticky='w')

start_month_letter = Label(window, text="월", width=1)
start_month_letter.grid(row=4, column=2, sticky='w')

start_date_input = tk.Entry(window, width=2)
start_date_input.grid(row=4, column=3, sticky='w')

start_date2_label = Label(window, text="일",width=1)
start_date2_label.grid(row=4, column=4, sticky='w')

end_date_label = Label(window, text=" 끝 날짜 ", anchor='w',width=10)
end_date_label.grid(row=5, column=0)

end_month_input = tk.Entry(window, width=2)
end_month_input.grid(row=5, column=1, sticky='w')

end_month_letter = Label(window, text="월", width=1)
end_month_letter.grid(row=5, column=2, sticky='w')

end_date_input = tk.Entry(window, width=2)
end_date_input.grid(row=5, column=3, sticky='w')

end_date2_label = Label(window, text="일",width=1)
end_date2_label.grid(row=5, column=4, sticky='w')

date_button = tk.Button(window, text= "이름\n날짜\n입력", width=5, command=put_DATE)
date_button.grid(row=3, column=6,rowspan=3,sticky='n'+'e'+'w'+'s', padx= 5)

execute_button = tk.Button(window, text= "실행", width=5, state="disabled", command=window.destroy)
execute_button.grid(row=0, column=7,rowspan=6,sticky='n'+'e'+'w'+'s')
execute_button.pack_forget()

window.mainloop()

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
Select(driver.find_element(By.CLASS_NAME, 'mtz-monthpicker-year')).select_by_value(str(2023))

if start_month % 3 == 0:
    tr = start_month // 3
    td = 3
else:
    tr = start_month // 3 + 1
    td = start_month % 3
driver.find_element('xpath', '/html/body/div[4]/table/tbody/tr[{}]/td[{}]'.format(tr, td)).click()
driver.find_element('xpath', '/html/body/div[3]/form/section[1]/div/div[2]/div/table/tbody/tr[1]/td[{}]'.format(start_date + 1)).click()
# 화면 전환
driver.switch_to.window(driver.window_handles[-1])

while 1:
    time_list = [1, 3, 5, 13, 18, 20, 22, 24]
    fixed_time_list = [7, 9, 11, 14, 16]
    result_list = time_list + fixed_time_list
    in_and_out()

    now_date = driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[2]/div[1]/div/input').get_attribute('value')
    if now_date == end_date:
        break
    # 빨간 글씨일 경우 패스
    if driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[2]/div[1]/span[2]').is_displayed():
        driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[2]/div[1]/div/a[2]/span').click()
        print(driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[2]/div[1]/div/a[2]/span').text)
        continue
    # 전체삭제
    is_xpath_exist(driver, '/html/body/form/div[2]/section[1]/div/div[3]/div[4]/div/div/ul/li[2]/a')
    driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[3]/div[4]/div/div/ul/li[2]/a').click()
    window_pop = Alert(driver)
    window_pop.accept()

    is_xpath_exist(driver, '/html/body/form/div[2]/section[1]/div/div[3]/div[5]/div/table/tbody/tr[1]/td[3]/span/label')
    for i in result_list:
        click_button(i)
    # 저장
    driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[3]/div[4]/div/div/ul/li[1]/a').click()
    # 다음 날짜
    driver.find_element('xpath', '/html/body/form/div[2]/section[1]/div/div[2]/div[1]/div/a[2]').click()