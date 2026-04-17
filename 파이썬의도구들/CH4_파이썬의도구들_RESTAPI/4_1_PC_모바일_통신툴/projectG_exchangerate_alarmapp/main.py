from selenium_manager import run_exchangerate_alarm

#0 환율 알람 값 설정
alarm_rate = float("1,419.20".replace(',', ''))

#1 run_exchangerate_alarm() 함수
run_exchangerate_alarm(alarm_rate)