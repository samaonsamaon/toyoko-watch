import os
import smtplib
from email.mime.text import MIMEText

import requests

DATES = [
    "2027-06-10",
    "2027-06-12",
    "2027-06-13",
    "2027-06-14",
    "2027-06-15",
]

HOTEL = "00208"

found = []

for d in DATES:
    end_date = d

    url = (
        "https://www.toyoko-inn.com/search/result/room_plan/"
        f"?hotel={HOTEL}"
        f"&start={d}"
        f"&end={end_date}"
        "&room=1"
        "&people=2"
        "&smoking=noSmoking"
        "&tab=roomType"
        "&sort=recommend"
    )

    r = requests.get(
        url,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    text = r.text

    no_room_texts = [
        "There are no rooms available",
        "満室",
    ]

    available = not any(x in text for x in no_room_texts)

    if available:
        found.append(f"{d}\n{url}")

if found:
    body = (
        "東横INNソウル東大門1で空室を検知しました\n\n"
        + "\n\n".join(found)
    )

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = "【空室発見】東横INN東大門1"
    msg["From"] = os.environ["EMAIL_ADDRESS"]
    msg["To"] = os.environ["EMAIL_ADDRESS"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(
            os.environ["EMAIL_ADDRESS"],
            os.environ["EMAIL_PASSWORD"],
        )
        smtp.send_message(msg)

    print("Mail sent")
else:
    print("No vacancy")
