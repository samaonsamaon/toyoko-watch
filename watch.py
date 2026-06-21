import requests

DATES = [
    "2027-06-10",
    "2027-06-12",
    "2027-06-13",
    "2027-06-14",
    "2027-06-15",
]

for d in DATES:
    url = (
        "https://www.toyoko-inn.com/search/result/room_plan/"
        f"?hotel=00208&start={d}"
        f"&end=2027-06-11"
        "&room=1&people=2"
        "&smoking=noSmoking"
        "&tab=roomType"
        "&sort=recommend"
    )

    r = requests.get(url, timeout=30)

    print(d)
    print(r.status_code)
