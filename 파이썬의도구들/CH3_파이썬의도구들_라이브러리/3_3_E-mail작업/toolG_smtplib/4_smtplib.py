import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email details
from_address = "kukjinman@gmail.com"
to_address = "kukjinman2@gmail.com"
subject = "Test Email"
body = "This is a test email with an attachment."

# Create the email
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Attach the file
filename = "test.txt"
with open(filename, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(part)

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "kukjinman@gmail.com"
smtp_password = "mbns gavv xekv hcpu"  # Replace with your actual password

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()