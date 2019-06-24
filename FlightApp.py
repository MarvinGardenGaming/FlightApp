import unirest
from CheapestFlight import *

response = unirest.post("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0",
  headers={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "5bed454f5amsh9a0c2efdc957585p179090jsna46d9ad2356f",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  params={
    "inboundDate": "2019-09-01",
    "children": 0,
    "infants": 0,
    "country": "US",
    "currency": "USD",
    "locale": "en-US",
    "originPlace": "SFO-sky",
    "destinationPlace": "PIT-sky",
    "outboundDate": "2019-09-01",
    "adults": 1
  }
)

locationHeader = str(response.headers.get('Location'))
splitArray = locationHeader.split("/")
arrayLength = len(splitArray)
SESSION_KEY = str(splitArray[arrayLength - 1])

response2 = unirest.get("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/" + SESSION_KEY + "?pageIndex=0&pageSize=5",
  headers={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "5bed454f5amsh9a0c2efdc957585p179090jsna46d9ad2356f",
    "Accept": "application/json"
  }
)

print response.code
print response2.code
#print response2.body

#Due to the nested lists and dicts in the HTTP Response the following code will pick out the individual pieces from the response.body
#Grab the Iteneraries from the response
iteneraries = response2.body["Itineraries"]

#Grab the first Itenerary
itenerariesDict = iteneraries[0]

#Grab the outbound and inbound leg ids
OutboundFlightID = itenerariesDict["OutboundLegId"]
InboundFlightID = itenerariesDict["InboundLegId"]
print ("Outbound Flight ID: " + OutboundFlightID)
print ("Inbound Flight ID: " + InboundFlightID)

#Grab the pricing options for that specific outbound inbound flight
pricingOptionsList = itenerariesDict["PricingOptions"]
pricingOption = pricingOptionsList[0]
price = str(pricingOption["Price"])
print ("Price: " + str(price))
currentCheapestFlight = CheapestFlight(price, 0)
currentCheapestFlight.printFlightInfo()

#Add loop that loops through each itinerary comparing prices
#Save Prices to currentCheapestFlight
#Send that flight info to heroku database

#Add a loop that does all of the previous stuff for the next 100 days
#Set that loop to run on a daily timer
