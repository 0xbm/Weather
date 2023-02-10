import requests


api_link = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = "&appid=7dc1e3959907f252891451585f715299"
api_units = "&units=metric"
api_lang = "&lang=pl"
api_city = input("City: ").lower().strip()

URL = api_link + api_city + api_key + api_units + api_lang
respone_dict = requests.get(URL).json()

print(f"{respone_dict['name']}, {respone_dict['sys']['country']}")
print(f"Temperature: {round(respone_dict['main']['temp'])} °C")
print(f"Feels_like: {round(respone_dict['main']['feels_like'])} °C")
print(f"Temperature max: {round(respone_dict['main']['temp_max'])} °C")
print(f"Temperature min: {round(respone_dict['main']['temp_min'])} °C")
print(f"Description: {respone_dict['weather'][0]['description']}")
print(f"Humidity: {respone_dict['main']['humidity']} %")
print(f"Pressure: {respone_dict['main']['pressure']} hPa")
print(f"Wind speed: {(respone_dict['wind']['speed']) * 3.6} km/h")
