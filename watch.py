import os
import requests
import smtplib
from email.mime.text import MIMEText

DATES = [
"2027-06-10",
"2027-06-11",
"2027-06-12",
"2027-06-13",
"2027-06-14",
"2027-06-15",
]

HOTEL_ID = "00291"

found = []

for start_date in DATES:
    year, month, day = map(int, start_date.split("-"))
from datetime import date, timedelta


end_date = str(date(year, month, day) + timedelta(days=1))

url = (
    "https://www.toyoko-inn.com/search/result/room_plan/"
    f"?hotel={HOTEL_ID}"
    f"&start={start_date}"
    f"&end={end_date}"
    "&room=1"
    "&people=2"
    "&smoking=noSmoking"
    "&tab=roomType"
    "&sort=recommend"
)

try:
    r = requests.get(
        url,
        timeout=30,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    text = r.text

    if (
        "There are no rooms available for Twin" not in text
        and "満室" not in text
    ):
        found.append(f"{start_date}\n{url}")

except Exception as e:
    print(f"Error: {e}")


if True:
    body = (
        "東横INNソウル東大門2で空室を検知しました。\n\n"
        + "\n\n".join(found)
    )

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = "【空室発見】東横INNソウル東大門2"
    msg["From"] = os.environ["EMAIL_ADDRESS"]
    msg["To"] = os.environ["EMAIL_ADDRESS"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(
            os.environ["EMAIL_ADDRESS"],
            os.environ["EMAIL_PASSWORD"]
        )
        smtp.send_message(msg)

    print("Mail sent")
else:
    print("No vacancy")
