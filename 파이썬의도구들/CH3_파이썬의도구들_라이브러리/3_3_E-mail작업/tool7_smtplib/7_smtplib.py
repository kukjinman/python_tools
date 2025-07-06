import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#1 SMTP 서버 설정
smtp_server = "smtp.gmail.com"
smtp_user = "kukjinman2@gmail.com"
smtp_password = "앱 비밀번호" # Google 계정의 앱 비밀번호 입력


#2 Email 설정
from_address = smtp_user
to_address = "kukjinman@gmail.com"
subject = "Test Email"
body = "파이썬 도구G 첨부파일 예시 메일입니다."

#3 Email 객체 생성
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = Header(s='파일첨부 메일송신 테스트', charset='utf-8')
msg.attach(MIMEText(body, 'plain',_charset='utf-8'))

#4 첨부파일 추가
filename = "attachment.txt"
part = MIMEBase('application', 'octet-stream')
attachment = open(filename, "rb")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename= {filename}")
msg.attach(part)


#5 SMTP 서버 연결 및 이메일 전송
try:
    server = smtplib.SMTP_SSL(smtp_server)
    server.login(smtp_user, smtp_password)
    server.send_message(msg)

    print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")

server.quit()