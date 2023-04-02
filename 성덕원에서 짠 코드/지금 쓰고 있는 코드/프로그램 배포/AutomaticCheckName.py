from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    global start_month, start_date, end_month, end_date, is_DATE
    start_month = int(start_month_input.get()) - 1
    start_date = int(start_date_input.get())
    end_month = int(end_month_input.get()) - 1
    end_date = int(end_date_input.get())

    is_DATE = True
    enable_execute_button()
    return
def is_xpath_exist(dr, xpath):
    try:
        # xpath가 로딩될 때 까지 10초 대기
        element = WebDriverWait(dr, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return True
    except:
        return False
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
def name_auto_check(driver, name):
    # 입소자 명단 클릭
    is_xpath_exist(driver, '//*[@id="content"]/div/div[1]/div[2]/div[2]/span/span[1]/span/span[2]')
    driver.find_element('xpath', '//*[@id="content"]/div/div[1]/div[2]/div[2]/span/span[1]/span/span[2]').click()

    # 이름 입력
    is_xpath_exist(driver, '/html/body/span/span/span[1]/input')
    driver.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys(name + Keys.ENTER)

    # 수분 버튼 클릭
    if driver.find_element('xpath', '//*[@id="content"]/div/div[1]/div[1]/div[1]/h2').text == "경관식 대상자":
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[1]/div[2]/div/button').click()

    # 시작 날짜 박스 클릭
    is_xpath_exist(driver, '//*[@id="start_dt"]')

    driver.find_element('xpath', '//*[@id="start_dt"]').click()
    driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]').click()

    # 시작 날짜 클릭
    Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_index(
        str(start_month))
    driver.find_element(By.LINK_TEXT,str(start_date)).click()

    # 종료 날짜 박스 클릭
    driver.find_element('xpath', '//*[@id="end_dt"]').click()
    driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]').click()

    # 종료 날짜 클릭
    Select(driver.find_element('xpath', '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_index(
        str(end_month))
    driver.find_element(By.LINK_TEXT,str(end_date)).click()

    # 검색 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/div[4]/button''[1]').click()

    # 며칠인지 확인
    tmp = 1
    cond = True
    while cond:
        cond = is_xpath_exist(driver, '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[7]'.format(tmp))
        if cond:
            tmp += 1
        else:
            tmp -= 1
    global count, start_column
    name_label = Label(window2, text=name, width=5)
    name_label.grid(row=count + 1, column=start_column)

    # 끝 이름 첫 이름 비교
    for i in range(1, tmp):
        name_list = driver.find_element('xpath',
            '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[7]'.format(i)).text.split()
        last_name = name_list[-1]
        name_list = driver.find_element('xpath',
            '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[7]'.format(i + 1)).text.split()
        first_name = name_list[0]

        if first_name != last_name:
            value_input = tk.Entry(window2)
            value_input.grid(row=count + 1, column=start_column + 1)
            value_input.insert(0, driver.find_element('xpath',
                                                      '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[4]'.format(
                                                          i + 1)).text)
            count+=1
    if count >= 40:
        count = -1
        start_column += 2


window = tk.Tk()
window.title("수분 자동 입력기")
window.geometry("325x110-700+400")
#window.resizable(False, False)

loginID_1 = "sdwon"
loginID_2 = StringVar()
loginID_3 = StringVar()
start_month = StringVar()
start_date = StringVar()
end_date = StringVar()
end_month = StringVar()

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

information_label = Label(window, text="아래에 시작 월과 끝 날짜를 입력해주세요")
information_label.grid(row=2, column=0, columnspan=7)

start_date_label = Label(window, text="시작 날짜 ", anchor= 'w',width=10)
start_date_label.grid(row=3, column=0)

start_month_input = tk.Entry(window, width= 2)
start_month_input.grid(row=3, column=1, sticky='w')

start_month_letter = Label(window, text="월", width=1)
start_month_letter.grid(row=3, column=2, sticky='w')

start_date_input = tk.Entry(window, width=2)
start_date_input.grid(row=3, column=3, sticky='w')

start_date2_label = Label(window, text="일",width=1)
start_date2_label.grid(row=3, column=4, sticky='w')

end_date_label = Label(window, text=" 끝 날짜 ", anchor='w',width=10)
end_date_label.grid(row=4, column=0)

end_month_input = tk.Entry(window, width=2)
end_month_input.grid(row=4, column=1, sticky='w')

end_month_letter = Label(window, text="월", width=1)
end_month_letter.grid(row=4, column=2, sticky='w')

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

window2 = tk.Tk()
window2.title("이름 확인 출력기")

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

# 경관식 대상자 클릭
is_xpath_exist(driver, '//*[@id="mainmenu"]/ul/li[4]/ul/li[5]/a')
driver.find_element('xpath', '//*[@id="mainmenu"]/ul/li[4]/ul/li[5]/a').click()

count = -1
start_column = 0
for i in range(len(name_list)):
    name_auto_check(driver, name_list[i])

window2.mainloop()