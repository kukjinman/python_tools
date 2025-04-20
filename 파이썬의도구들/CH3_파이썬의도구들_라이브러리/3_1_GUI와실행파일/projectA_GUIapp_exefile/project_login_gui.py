import tkinter as tk
from tkinter import messagebox

#6 on_login_click 함수
def on_login_click(event=None):
    if event:
        print(f"Event key symbol: {event.keysym}")
        print(f"Event key code: {event.keycode}")
    # entry에 입력된 username과 password를 가져옵니다.
    username = entry_username.get()
    password = entry_password.get()
    print(f"Username: {username}, Password: {password}")
    # 환영 메시지를 표시합니다.
    messagebox.showinfo("Welcome", f"Welcome, {username}")

#1 메인 윈도우
root = tk.Tk()
root.title("Login GUI")
root.geometry("300x200")

#2 Username 라벨과 엔트리
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)


#3 Password 라벨과 엔트리
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

#4 로그인 버튼
button_login = tk.Button(root, text="Login", command=on_login_click)
button_login.pack(pady=20)

#5 Enter키 이벤트
root.bind('<Return>', on_login_click)

#7 GUI 애플리케이션 실행
root.mainloop()