from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#1 Selenium의 webdriver를 사용한 browser 객체 생성
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=opt)

#2 browser로 네이버 금융 페이지 열기
browser.get('https://finance.naver.com/')
time.sleep(2)

#3 검색창에 LG전자 검색
search_input_box = browser.find_element(by=By.CSS_SELECTOR, value='#stock_items')
search_input_box.send_keys("LG전자")
search_input_box.submit()
time.sleep(2)

#4 검색 결과 출력
stock_name = browser.find_element(by=By.CSS_SELECTOR, value='#content > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.tit > a')
current_price = browser.find_element(by=By.CSS_SELECTOR, value='#content > div:nth-child(4) > table > tbody > tr:nth-child(1) > td:nth-child(2)')
print(stock_name.text)
print(current_price.text)

#5 browser 종료
# browser.quit()
