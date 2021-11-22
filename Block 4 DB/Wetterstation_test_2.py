import requests
import json

weather_results = []
key = '42eaa3bc811e19a642f24952c37b080c'
cities = ['Winterthur']

def weather_get(apikey, city):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={},canada&APPID={}'.format(city, apikey))
    return(r.text)

def get_temp(arg):
    for items in arg:
        for key, value in items['main'].items():
            if key=='temp':
                return(value)

def get_pressure(arg):
    for items in arg:
        for key, value in items['main'].items():
            if key=='pressure':
                return(value)

def get_temp_min(arg):
    for items in arg:
        for key, value in items['main'].items():
            if key=='temp_min':
                return(value)

print(get_temp(arg=""))
#
# import requests
#
#
# class Wetterstation:
#
#     def __init__(self, appid, stadt, einheiten, url):
#         super().__init__()
#         self.appid = appid
#         self.stadt = stadt
#         self.einheiten = einheiten
#         self.url = url
#
#     def __str__(self):
#         return f"\nDie Abfrage URL für {self.stadt} ist: " \
#                + self.url.format(appid=self.appid, einheiten=self.einheiten, stadt=self.stadt)
#
#     def __eq__(self, other):
#         pass
#
#     def temperatur_aktuell(self):
#         # temperatur_aktuell ruft die "Current Weather Data" API von openweathermap auf
#         request_url = self.url
#         # die Übergebene Basis-URL wird mit dem API Key, der gewünschten Einheiten und der gewählten Stadt,
#         # was zum gewünschten Aufruf führt
#         api_request = request_url.format(appid=self.appid, einheiten=self.einheiten, stadt=self.stadt)
#         api_response_1 = requests.get(api_request).json()
#         # Rundung der Temperaturangaben, könnte man über eine Schalufe machen
#         temp = api_response_1['main']['temp']
#         feels_like = api_response_1['main']['feels_like']
#         temp_min = api_response_1["main"]["temp_min"]
#         temp_max = api_response_1["main"]["temp_max"]
#         print("\nHier sind die aktuellen Temperaturen von " + self.stadt,
#               "\nDie akuelle Temperatur beträgt:    " + str(temp) + chr(176) + "C",
#               "\nFühlt sich an wie:                 " + str(feels_like) + chr(176) + "C")
#         return api_response_1
#
#     def zusaetzliche_angaben(self):
#         request_url = self.url
#         api_request = request_url.format(appid=self.appid, einheiten=self.einheiten, stadt=self.stadt)
#         api_response_2 = requests.get(api_request).json()
#         truebung = api_response_2['clouds']['all']
#         wind_geschwindigkeit = api_response_2['wind']['speed']
#         print("\nZusätliche Wetterangaben von " + self.stadt,
#               "\nDie akuelle Trübung beträgt:               " + str(truebung) + "%",
#               "\nDie akuelle Windgeschwindigkeit beträgt:   " + str(wind_geschwindigkeit) + "km/h")
#         return api_response_2
#
#
# if __name__ == '__main__':
#     abfrage1 = Wetterstation(
#         appid="42eaa3bc811e19a642f24952c37b080c",
#         url="http://api.openweathermap.org/data/2.5/weather?appid={appid:32s}&units={einheiten:6s}&q={stadt:32s}",
#         einheiten="metric",
#         stadt=input("Bitte geben Sie eine Stadt ein: "))
#     abfrage1.temperatur_aktuell()
#     abfrage1.zusaetzliche_angaben()
#     print(abfrage1)
#
# # ------------------------------------------------------------------------------------------------------------------
# # Tests
# # ------------------------------------------------------------------------------------------------------------------
#
# # def test_temperatur_aktuell():
# #     print("\n")
# #     Wetterstation.temperaturAktuell(
# #          stadt="Winterthur",
# #          url="http://api.openweathermap.org/data/2.5/weather?appid=42eaa3bc811e19a642f24952c37b080c&units=metric&q=")
# #     print("Hier sind die aktuellen Temperaturen von " + self.stadt,
# #           "\nDie akuelle Temperatur beträgt:    " + str(temp) + chr(176),
# #           "\nFühlt sich an wie:                 " + str(feels_like) + chr(176))
# #
# # def test_zusaetzliche_angaben():
# #     print("\n")
# #     Wetterstation.temperatur_aktuell(appid="42eaa3bc811e19a642f24952c37b080c",
# #              url="http://api.openweathermap.org/data/2.5/weather?appid={appid:32s}&units={einheiten:32s}&q={stadt:32s}",
# #              einheiten="metric",
# #              stadt=input("Bitte Stadt eingeben: ")
# #     print("Zusätliche Wetterangaben von: " + self.stadt,
# #           "\nDie akuelle Trübung beträgt:               " + str(truebung) + "%",
# #           "\nDie akuelle Windgeschwindigkeit beträgt:   " + str(wind_geschwindigkeit) + "km/h")
#
# # def test_dunder__str__():
# #     print("\n")
# #     abfrage1 = Wetterstation(
# #         url="http://api.openweathermap.org/data/2.5/weather?appid=42eaa3bc811e19a642f24952c37b080c&units=metric&q=",
# #         stadt="Winterthur")
# #     print(abfrage1)
