import requests
r=requests.get("https://my.itmo.ru/")
print(r.text)