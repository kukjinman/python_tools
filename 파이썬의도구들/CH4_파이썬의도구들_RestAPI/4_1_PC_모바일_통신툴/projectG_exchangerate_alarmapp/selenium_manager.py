from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from twilio_manager import send_whatsapp_message

def get_exchangerate():
    print("get_exchangerate() is called")

    #1 Selenium의 webdriver를 사용한 browser 객체 생성
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    opt.add_argument("headless")  # Headless 모드 설정
    browser = webdriver.Chrome(options=opt)

    #2 browser로 네이버 금융 페이지 열기
    browser.get("https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_USDKRW")

    exchange_rate = browser.find_element(By.CSS_SELECTOR, "#content > div.section_calculator > table:nth-child(4) > tbody > tr > td:nth-child(1)")
    print(exchange_rate.text)

    return float(exchange_rate.text.replace(',', ''))

def run_exchangerate_alarm(alarm_value):

    while(True):
        print("run_exchangerate_alarm() is called")
        #1 Selenium을 사용하여 환율 정보를 가져오기
        current_rate = get_exchangerate()
        print(f"Current exchange rate: {current_rate}")

        #2 현재 환율이 알람 값보다 높은지 확인
        if current_rate > alarm_value:
            print(f"Alarm! Current exchange rate ({current_rate}) is higher than the set value ({alarm_value}).")

            #3 WhatsApp 메시지 전송
            send_whatsapp_message(current_rate, alarm_value)
            break
        sleep(1)


