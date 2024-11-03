import tkinter as tk
from tkinter import messagebox

# 버튼 클릭 시 호출되는 함수
def on_button_click():
    messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

# 메인 윈도우 생성
root = tk.Tk()
root.title("파이썬 GUI 예제")
root.geometry("320x200")  # 창 크기 설정
root.configure(bg="#2c2c2c")  # 배경색을 검정으로 설정

# 텍스트 라벨 생성
label1 = tk.Label(root, text="파이썬의 도구들", font=("Helvetica", 24, "bold"), bg="#2c2c2c", fg="#ffffff")
label1.grid(row=0, column=0, pady=(10, 0), sticky="nsew")

label2 = tk.Label(root, text="파이썬 GUI Test", font=("Helvetica", 18), bg="#2c2c2c", fg="#ffffff")
label2.grid(row=1, column=0, pady=(10, 0), sticky="nsew")

# 버튼 생성
button = tk.Button(root, text="클릭하세요", command=on_button_click, bg="#2980b9", fg="#ffffff", font=("Helvetica", 14), bd=0)
button.grid(row=2, column=0, pady=(20, 0), padx=5, sticky="nsew")

# 종료 버튼 추가
exit_button = tk.Button(root, text="종료", command=root.quit, bg="#e74c3c", fg="#ffffff", font=("Helvetica", 14), bd=0)
exit_button.grid(row=3, column=0, pady=(10, 10), padx=5, sticky="nsew")

# 행과 열의 비율 설정
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

# GUI 루프 시작
root.mainloop()
