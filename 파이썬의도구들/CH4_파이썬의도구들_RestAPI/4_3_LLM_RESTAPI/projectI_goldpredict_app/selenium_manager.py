from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

#1 get_gold_data 함수 정의
def get_gold_data():

    gold_data = ""

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    opt.add_argument("headless")
    browser = webdriver.Chrome(options=opt)

    #2 browser로 네이버 금융에서 KODEX 골드선물 페이지 열기
    browser.get("https://finance.naver.com/item/main.naver?code=132030")

    #3 금값 데이터의 테이블에서 tr 요소들 추출
    trs = browser.find_elements(By.CSS_SELECTOR, "#content > div.section.etf_nav > table > tbody > tr")

    for tr in trs:
        #4 각 tr에서 td 요소 추출
        tds = tr.find_elements(By.TAG_NAME, "td")

        if len(tds) > 2:
            #5 td 요소에서 텍스트 추출
            date = tds[0].text
            price = tds[1].text
            print(f"날짜: {date}, 가격: {price}")

            #6 gold_data에 날짜와 가격 정보를 추가
            gold_data += f"날짜: {date}, 가격: {price}\n"

    return gold_data