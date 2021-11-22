# Quellen:
# https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python
# https://www.simplifiedpython.net/openweathermap-api-python/#OpenWeatherMapAPI_Python_Tutorial_-Access_Current_Weather_Data_For_One_Location
# https://code-maven.com/openweathermap-api-using-python
# https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
# https://www.codeunderscored.com/get-weather-report-python-openweathermap-api/

import json
import requests

# appid= "42eaa3bc811e19a642f24952c37b080c"
stadt = "Winterthur"
url = "http://api.openweathermap.org/data/2.5/weather?appid=42eaa3bc811e19a642f24952c37b080c&units=metric&q=" + stadt


api_response = requests.get(url).json()
truebung = api_response['clouds']['all']
wind_geschwindigkeit = api_response['wind']['speed']
for entry in api_response['clouds']:
    truebung = entry['clouds']['all']
    clouds = {'all', truebung}
    api_response['clouds'].append(clouds)

print("Zusätliche Wetterangaben von: " + stadt,
"\nDie akuelle Trübung beträgt:               " + str(truebung) + "%")
# "\nDie akuelle Windgeschwindigkeit beträgt:   " + str(wind_geschwindigkeit) + "km/h")

# stadt = "Winterthur"
# base_url = "http://api.openweathermap.org/data/2.5/weather?appid=42eaa3bc811e19a642f24952c37b080c&units=metric&q={search:2s}"
# requestStr = base_url.format(search=stadt)
# responseStr = requests.get(requestStr)
# jsonResponse = json.loads(responseStr.text)
# for entry in jsonResponse['main']:
#     temp_min = entry['main']['temp_min']
#     temp_max = entry['main']['temp_max']
#     feuchtigkeit = entry['main']['humidity']
#     main = {'temp_min': temp_min,
#              'temp_max': temp_max,
#              'humidity': feuchtigkeit
#           }
#
#     jsonResponse['main'].append(main)
#
#     print("\nStadt   : ", stadt)
#     print("  Temperatur Minimum    :", temp_min)
#     print("  Temperatur Maxumum    :", temp_max)
#     print("  Feuchtigkeit          :", feuchtigkeit)


# bewoelkt = entry['clouds']['all']
# wind_geschwindigkeit = entry['wind']['speed']
# zeitpunkt_abfrage = entry['dt']
#
# clouds = {'all': bewoelkt}
# wind = {'speed': wind_geschwindigkeit}
# dt = {'dt': zeitpunkt_abfrage}
#
# jsonResponse['clouds'].append(clouds)
# jsonResponse['wind'].append(wind)
# jsonResponse['dt'].append(dt)

# stadt = "Winterthur"
# url = base_url + stadt
# api_response = requests.get(url).json()
# temp = api_response['main']['temp']
# feels_like = api_response['main']['feels_like']
# temp_min = api_response["main"]["temp_min"]
# temp_max = api_response["main"]["temp_max"]
# print("Hier sind die aktuellen Temperaturen von " + stadt,
#       "\nDie akuelle Temperatur beträgt:    " + str(temp) + chr(176),
#       "\nFühlt sich an wie:                 " + str(feels_like) + chr(176))

# def TemperaturAktuell():
#     stadt = "Winterthur"
#     url = base_url + stadt
#     api_response = requests.get(url).json()
#     temp = round((api_response['main']['temp']) - 273.15, 1)
#     feels_like = round((api_response['main']['feels_like']) - 273.15, 1)
#     print("Hier sind die aktuellen Temperaturen von " + stadt,
#           "\nDie akuelle Temperatur beträgt:    " + str(temp) + chr(176),
#           "\nFühlt sich an wie:                 " + str(feels_like) + chr(176))
#
# TemperaturAktuell()
#
#         self.stadt = stadt
#         self.url = base_url + stadt
#         self.api_response = requests.get(self.url).json()
#         temp = round((self.api_response['main']['temp']) - 273.15, 1)
#         feels_like = round((self.api_response['main']['feels_like']) - 273.15, 1)
#         print("Hier sind die aktuellen Temperaturen von " + stadt,
#               "\nDie akuelle Temperatur beträgt:    " + str(temp_celcius) + chr(176),
#               "\nFühlt sich an wie:                 " + str(feels_like_celcius) + chr(176))
