from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings

warnings.filterwarnings("ignore")


def is_xpath_exist(dr, xpath):
    try:
        # xpath가 로딩될 때 까지 10초 대기
        element = WebDriverWait(dr, 3).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return True
    except:
        return False


def input_month(op):
    while 1:
        if op == 1:
            start_month = int(input("검색 시작 월을 입력해주세요 : ")) - 1
            if (start_month >= 0) and (start_month <= 11):
                return start_month
            else:
                print("다시 입력해주세요")
        elif op == 2:
            end_month = int(input("검색 종료 월을 입력해주세요 : ")) - 1
            if (end_month >= 0) and (end_month <= 11):
                return end_month
            else:
                print("다시 입력해주세요")


def input_date(op):
    while 1:
        if op == 1:
            start_date = int(input("검색 시작 일을 입력해주세요 : "))
            if (start_date >= 1) and (start_date <= 31):
                return start_date
            else:
                print("다시 입력해주세요")
        elif op == 2:
            end_date = int(input("검색 종료 일을 입력해주세요 : "))
            if (end_date >= 1) and (end_date <= 31):
                return end_date
            else:
                print("다시 입력해주세요")


def water_auto_check(driver, name):

    # 입소자 명단 클릭
    is_xpath_exist(driver, '//*[@id="content"]/div/div[1]/div[2]/div[2]/span/span[1]/span/span[2]')
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/div[2]/span/span[1]/span/span[2]').click()

    # 이름 입력
    is_xpath_exist(driver, '/html/body/span/span/span[1]/input')
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(name + Keys.ENTER)

    # 수분 버튼 클릭
    if driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[1]/div[1]/h2').text == "경관식 대상자":
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[1]/div[2]/div/button').click()

    # 시작 날짜 박스 클릭
    is_xpath_exist(driver, '//*[@id="start_dt"]')

    driver.find_element_by_xpath('//*[@id="start_dt"]').click()
    driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[1]/div/select[2]').click()

    # 시작 날짜 클릭
    Select(driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_index(
        str(start_month))
    driver.find_element_by_link_text(str(start_date)).click()

    # 종료 날짜 박스 클릭
    driver.find_element_by_xpath('//*[@id="end_dt"]').click()
    driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[1]/div/select[2]').click()

    # 종료 날짜 클릭
    Select(driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[1]/div/select[2]')).select_by_index(
        str(end_month))
    driver.find_element_by_link_text(str(end_date)).click()

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

    print("------------------------------------------------------------------------------------------------------------------")
    print("{}님".format(name), end=" ")
    print()

    # 끝 수분 첫 수분 비교
    for i in range(1, tmp):
        total_water = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[5]'.format(i)).text
        first_water = total_water
        total_water = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[5]'.format(i + 1)).text
        last_water = total_water

        time_cc = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[6]/table/tbody/tr/td[1]'.format(i)).text
        first_time = time_cc
        time_cc = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[6]/table/tbody/tr/td[1]'.format(i + 1)).text
        last_time = time_cc

        if (first_water == last_water) and (first_time == last_time):

            print(driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[2]/div/table/tbody/tr[{}]/td[4]'.format(i + 1)).text, end="")
            print("일 잘못됨")

    print("프로그램 종료")
    print("------------------------------------------------------------------------------------------------------------------")


# 일단 시작 날짜 입력
start_month = input_month(1)
start_date = input_date(1)

end_month = input_month(2)
end_date = input_date(2)

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

# 경관식 대상자 클릭
is_xpath_exist(driver, '//*[@id="mainmenu"]/ul/li[4]/ul/li[5]/a')
driver.find_element_by_xpath('//*[@id="mainmenu"]/ul/li[4]/ul/li[5]/a').click()
"""
# 입소자 명단 클릭
is_xpath_exist(driver, '//*[@id="conten"]/div/div[1]/div[2]/div[2]/span/span[1]/span/span[2]')
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/div[2]/span/span[1]/span/span[2]').click()
"""
name_list = ['강복순', '강순남', '강재현', '고연님', '김갑순', '김귀임', '김남석', '김단례', '김도순', '김분임', '김성순', '김애덕', '김춘선', '김춘자', '남정순', '문복선', '박당녀', '박형봉', '방남례', '서옥순', '송덕순', '송영자', '심삼남', '양명순', '양소례', '염옥순', '우복인', '유복', '유승숙', '이건주', '이상수', '이선미', '이얌순', '이양님', '이정애', '임계순', '임순덕', '전신자', '전점례', '정귀모', '정중헌', '정해님', '조대섭', '주정애', '진병금', '최순옥', '최정자', '탁봉순', '하태순', '한순임', '허경임', '허야무']

for i in range(len(name_list)):
    water_auto_check(driver, name_list[i])