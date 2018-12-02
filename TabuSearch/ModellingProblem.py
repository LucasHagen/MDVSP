import numpy as np

class Solution():
    def __init__(self, nDepots: int, nTrips: int, maxBus: list):
        self.nDepots = nDepots
        self.nTrips = nTrips
        self.maxBus = maxBus
        self.solutionDepots = np.zeros(shape = (nDepots, nTrips), dtype = int)  #Represents if a bus is going out of the depot to a trip. Initially has only zeros, and has binary values
        self.solutionTrips = np.zeros(shape = (nTrips, nTrips), dtype = int)    #Represents if a bus is going from a trip to another one.
        self.value = -1 #Minus one means that the actual value has not been calculated
        

    def generateRandomSolution(self, seedSolution):
        pass
    
    def checkRestictionsAndValue(self, depotToTrip, tripToDepot, tripToTrip):
        """Returns if a problem is in conformity with it's restrictions, and refresh the value of the value function"""
        self.value = 0
        
        #Restricion: We must pass through every trip
        listOFTrips = np.zeros(shape=self.nTrips, dtype=int)    #We start filling it with zeros, and we'll fill it with the amount of ocourrences in it as we progress through the tables

        # We must respect the limit of bus in each depot
        for d in range(self.nDepots):
            actualBusCount = 0
            
            for t in range(self.nTrips):
                if (self.solutionDepots[d][t] > 0):
                    actualBusCount+=1
                    self.value+=depotToTrip[d][t]
                    else:
                        return False
                    listOFTrips[t] += 1

            if (actualBusCount > self.maxBus[d]):
                return False
        
        # We need to check where each trip is going
        for t1 in range(self.nTrips):
            #We need to go through the solutionTruos and check the trips, problem is, we also need to keep track of the graph because the
            #bus that's going needs to go back to the depot, and i don't know how to make that efficiently
            #Also, we need to make sure only ONE bus goes through each trip, and only one bus leaves from it
            #Since it will be impossible to keep track of where the bus will need to go back
            pass


        
            