import json

import requests

r=requests.get("https://api.covidtracking.com/v1/us/daily.json")
data=json.loads(r.text)
death=data[0]["death"]
negative=data[0]["negative"]
positive=data[0]["positive"]
hospital=data[0]["hospitalizedCurrently"]
total=data[0]["totalTestResults"]
print(f"Смертей от Covid-19 в США на 07.03.2021:{death}\n"
      f"Количество отрицательных тестов в США на 07.03.2021:{negative}\n"
      f"Количество положительных тестов в США на 07.03.2021:{positive}\n"
      f"Общее количество проведенных тестов в США на 07.03.2021:{total}\n"
      f"Количество госпитализированных в США 07.03.2021:{hospital}")
