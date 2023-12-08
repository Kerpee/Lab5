import requests
city_data=input("Введите город:")
def get_weather(city,token):
    r=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f2c3446a7fedc04e3848b74b7df782bf&units=metric")
    data=r.json()
    city=data["name"]
    temperature=data['main']['temp']
    humid=data['main']["humidity"]
    pressure=data['main']['pressure']
    print(f"Город: {city}"+"\n"+f"Температура сейчас: {temperature}°C"+"\n"+f"Влажность сейчас: {humid}%"+"\n"+f"Давление сейчас: {pressure}")
get_weather(city_data,None)