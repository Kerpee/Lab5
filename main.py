import requests
from TOKEN import token

city_data=input("Введите город:")
token=token
def get_weather(city,token):
    r=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
    data=r.json()
    city=data["name"]
    temperature=data['main']['temp']
    humid=data['main']["humidity"]
    pressure=data['main']['pressure']
    return (f"Город: {city}"+"\n"+f"Температура сейчас: {temperature}°C"+"\n"+f"Влажность сейчас: {humid}%"+"\n"+f"Давление сейчас: {pressure}")
print(get_weather(city_data,token))