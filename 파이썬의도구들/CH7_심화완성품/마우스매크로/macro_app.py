import pyautogui
import time

# 반복 횟수 설정
repeat_count = 10

# 마우스 이동 및 클릭 반복
while(True):
    # 현재 위치 출력
    print(f"{pyautogui.position()}")

    # 마우스 이동 (x, y 좌표로 이동)
    pyautogui.moveTo(300, 300, duration=0.5)  # (x=300, y=300)으로 0.5초 동안 이동
    pyautogui.click()  # 클릭

    # 다른 위치로 이동
    pyautogui.moveTo(500, 500, duration=0.5)  # (x=500, y=500)으로 0.5초 동안 이동
    pyautogui.click()  # 클릭

    # 대기 시간
    time.sleep(5)  # 5초 대기