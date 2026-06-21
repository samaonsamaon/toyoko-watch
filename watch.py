import os
import smtplib
from email.mime.text import MIMEText

msg = MIMEText(
    "東横イン監視システムのテストメールです。",
    "plain",
    "utf-8"
)

msg["Subject"] = "【テスト】Toyoko Watch"
msg["From"] = os.environ["EMAIL_ADDRESS"]
msg["To"] = os.environ["EMAIL_ADDRESS"]

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(
        os.environ["EMAIL_ADDRESS"],
        os.environ["EMAIL_PASSWORD"]
    )
    smtp.send_message(msg)

print("Test mail sent")
