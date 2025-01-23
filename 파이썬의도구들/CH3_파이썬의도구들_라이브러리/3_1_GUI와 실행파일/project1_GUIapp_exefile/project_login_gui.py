import tkinter as tk
from tkinter import messagebox

#1 로그인 버튼을 클릭했을 때, enter키가 눌렸을 때 호출되는 함수입니다.
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

#2 메인 윈도우를 생성합니다.
root = tk.Tk()
root.title("Login GUI")
root.geometry("300x200")

#3 사용자 이름을 위한 label을 생성합니다.
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

#4 사용자 이름을 입력받기 위한 입력 entry를 생성합니다.
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

#5 비밀번호를 위한 label을 생성합니다.
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

#6 비밀번호를 입력받기 위한 entry를 생성합니다.
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

#7 로그인 버튼을 생성합니다.
button_login = tk.Button(root, text="Login", command=on_login_click)
button_login.pack(pady=20)

#8 Enter 키를 눌렀을 때 on_login_click 함수를 호출하도록 바인딩합니다.
root.bind('<Return>', on_login_click)

#9 GUI 애플리케이션을 실행합니다.
root.mainloop()