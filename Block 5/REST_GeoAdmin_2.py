import requests
import json

searchCriteria = "Peterliwiese%203"

def getResults_geoAdmin(searchCriteriaEncoded, doTrace = False):
    serviceURL = "https://api3.geo.admin.ch/1912100956/rest/services/ech/SearchServer?sr=2056&searchText={search:2s}&lang=en&type=locations"
    appId = ""
    requestStr = serviceURL.format(search=searchCriteriaEncoded)
    responseStr = requests.get(requestStr)
    jsonResponse = json.loads(responseStr.text)
    # print("Request:\n", requestStr) if doTrace else False
    # print("Response:\n", jsonResponse, "\n") if doTrace else False
    returnJSON = {'criteria' : searchCriteriaEncoded,
                  'count' : int(len(jsonResponse['results'])),
                  'results' : []}

    recNr = 1
    # print("Parsed values (Records found:{recCount:2d}):".format(recCount=len(jsonResponse['results'])))
    for entry in jsonResponse['results']:
        details = entry['attrs']['detail']
        lon = entry['attrs']['lon']
        lat = entry['attrs']['lat']
        x = entry['attrs']['x']
        y = entry['attrs']['y']
        details = {'details' : details,
                   'longitude' : lon,
                   'latitude' : lat,
                   'ch_x' : x,
                   'ch_y' : y}
        returnJSON['results'].append(details)
        print("\nRecord No: ", recNr) if doTrace else False
        print("  detail  :", details) if doTrace else False
        print("  lon     :", lon) if doTrace else False
        print("  lat     :", lat) if doTrace else False
        print("  x       :", x) if doTrace else False
        print("  y       :", y) if doTrace else False
        recNr += 1
    return returnJSON