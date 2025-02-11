import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

output_dir_path = 'output'

def requestTo_send_email(from_address, password, to_address, subject, body, attached_file_path):
    smtp_server = "smtp.gmail.com"
    smtp_user = from_address
    smtp_password = password


    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = Header(s=subject, charset='utf-8')
    msg.attach(MIMEText(body, 'plain', _charset='utf-8'))

    filename = f"{output_dir_path}/{attached_file_path}"
    part = MIMEBase('application', 'vnd.openxmlformats-officedocument.wordprocessingml.document')
    attachment = open(filename, "rb")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    print(f"attached_file_path: {attached_file_path}")
    encoded_filename = Header(attached_file_path, 'utf-8').encode()
    part.add_header('Content-Disposition', f'attachment; filename="{encoded_filename}"')
    msg.attach(part)

    try:
        server = smtplib.SMTP_SSL(smtp_server)
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

    server.quit()