import requests
import json
from lxml import etree
import time

searchCriteria = "Peterliwiese%2033"

# map.geo.admin: https://api3.geo.admin.ch/1912100956/rest/services/ech/SearchServer?sr=2056&searchText=Peterliwiese%2033&lang=en&type=locations
# API: https://api3.geo.admin.ch/services/sdiservices.html
serviceURL = "https://api3.geo.admin.ch/1912100956/rest/services/ech/SearchServer?sr=2056&searchText={search:2s}&lang=en&type=locations"
appId = ""
requestStr = serviceURL.format(search=searchCriteria)
responseStr = requests.get(requestStr)
jsonResponse = json.loads(responseStr.text)
print("Request:\n", requestStr)
print("Response:\n", jsonResponse, "\n")
print("Parsed values:")
for entry in jsonResponse['results']:
    print("  detail  :", entry['attrs']['detail'])
    print("  lon     :", entry['attrs']['lon'])
    print("  lat     :", entry['attrs']['lat'])

print("-----------------------------------------------------------------")
# search.ch: https://tel.search.ch/api/?q=Walter%20Rothlin%208855&key=8e8a84fd0f10d3b44920e49bc3b06a37
# API:  https://tel.search.ch/api/help
searchCriteria = "Walter%20Rothlin%208855"
appId = "8e8a84fd0f10d3b44920e49bc3b06a37"
serviceURL = "https://tel.search.ch/api/?q={search:2s}&key={appId:2s}"
requestStr = serviceURL.format(search=searchCriteria, appId=appId)
responseStr = requests.get(requestStr).content

print("Request:\n", requestStr)
print("Response:\n", responseStr, "\n")

print("Parsed values:")
namespaces = {'tel': 'http://tel.search.ch/api/spec/result/1.0/'} # add more as needed
dom = etree.HTML(responseStr)
value = dom.xpath('//entry')
print("  Elemnts found  :", len(value))

for aEntry in value:
    telNr = aEntry.find("name", namespaces).text
    zip = aEntry.find("zip", namespaces).text
    content = aEntry.find("content").text
    print("  aEntry  :", aEntry)
    print("  Content :", content)
    print("  telNr   :", telNr)
    print("  Zip     :", zip)
    print()

print("-----------------------------------------------------------------")

# Google API:    https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Peterliwiese+33&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyDAKgrjrKNmBPu47TUFP-x8hY_jp2Ainbk
searchCriteria = "Peterliwiese+33"
appId = "AIzaSyDAKgrjrKNmBPu47TUFP-x8hY_jp2Ainbk"
serviceURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={search:2s}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={appId:2s}"
requestStr = serviceURL.format(search=searchCriteria, appId=appId)
responseStr = requests.get(requestStr)
jsonResponse = json.loads(responseStr.text)
print("Request:\n", requestStr)
print("Response:\n", jsonResponse, "\n")