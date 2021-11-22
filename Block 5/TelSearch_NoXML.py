import requests
import json
from lxml import etree
import time

# search.ch: https://tel.search.ch/api/?q=Walter%20Rothlin%208855&key=8e8a84fd0f10d3b44920e49bc3b06a37
# API:  https://tel.search.ch/api/help
searchCriteria = "elchweg"
appId = "8e8a84fd0f10d3b44920e49bc3b06a37"
serviceURL = "https://tel.search.ch/api/?q={search:2s}&key={appId:2s}"
requestStr = serviceURL.format(search=searchCriteria, appId=appId)
responseStr = requests.get(requestStr).content

print("Request:\n", requestStr)
print("Response:\n", responseStr, "\n")

print("Parsed values:")
namespaces = {'tel': 'http://tel.search.ch/api/spec/result/1.0/',
                     'openSearch':'http://a9.com/-/spec/opensearchrss/1.0/' } # add more as needed
dom = etree.HTML(responseStr)
value = dom.xpath('//entry')
print("  totResults  :", len(value))

for aEntry in value:
    telNr = aEntry.find("phone", namespaces).text
    zip = aEntry.find("zip", namespaces).text
    content = aEntry.find("content").text
    print("  aEntry  :", aEntry)
    print("  Content :\n   ", content)
    print("  telNr   :", telNr)
    print("  Zip     :", zip)
    print()

print("-----------------------------------------------------------------")