#1 준비 단계
import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

#2 메인 윈도우 생성
root = tk.Tk()
root.title("파이썬 GUI 예제")

# 기존에 고정된 geometry 설정을 화면 중앙 배치로 바꿉니다
window_width = 320
window_height = 200
# 창 크기 먼저 설정한 뒤 화면 크기 정보를 읽어 중앙 좌표 계산
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
pos_x = (screen_width - window_width) // 2
pos_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

root.configure(bg="#2c2c2c")  # 배경색을 어두운 회색으로 설정

#3 텍스트 라벨 생성
label1 = tk.Label(root, text="파이썬의 도구들", font=("Helvetica", 24, "bold"), bg="#2c2c2c", fg="#ffffff")
label1.grid(row=0, column=0, pady=(10, 0), sticky="nsew")

label2 = tk.Label(root, text="파이썬 GUI Test", font=("Helvetica", 18), bg="#2c2c2c", fg="#ffffff")
label2.grid(row=1, column=0, pady=(10, 0), sticky="nsew")

#4 클릭하세요 버튼 생성
button = tk.Button(root, text="클릭하세요", command=on_button_click, bg="#2980b9", fg="#ffffff", font=("Helvetica", 14), bd=0)
button.grid(row=2, column=0, pady=(20, 0), padx=5, sticky="nsew")

#5 종료 버튼 추가
exit_button = tk.Button(root, text="종료", command=root.quit, bg="#e74c3c", fg="#ffffff", font=("Helvetica", 14), bd=0)
exit_button.grid(row=3, column=0, pady=(10, 10), padx=5, sticky="nsew")

# #6 행과 열의 비율 설정
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

# GUI 루프 시작
root.mainloop()
