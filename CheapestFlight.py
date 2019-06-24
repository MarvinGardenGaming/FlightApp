class CheapestFlight :
    def __init__(self, p, i):
        self.price = p
        self.itineraryIndex = i
        return
    def printFlightInfo(self):
        print ("Price is: " + str(self.price) + " Index is: " + str(self.itineraryIndex))

