from selenium_manager import run_exchangerate_alarm


alarm_rate = float("1,419.20".replace(',', ''))
run_exchangerate_alarm(alarm_rate)