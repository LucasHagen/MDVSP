import numpy as np
import random

class ListBus():
    def __init__(self, firstTrip: int):
        self.depot = -1 #Not decided yet
        self.path = [firstTrip]
    
    def insertNewTrip(self, trip: int):
        self.path.append(trip)
    
    def insertNewDepot(self, depot: int):
        self.depot = depot

class Solution():
    def __init__(self, nDepots: int, nTrips: int, maxBus: list, depotToTrip: np.ndarray, tripToDepot: np.ndarray, tripToTrip: np.ndarray):
        self.nDepots = nDepots
        self.nTrips = nTrips
        self.maxBus = maxBus
        
        self.depotToTrip = depotToTrip
        self.tripToTrip = tripToTrip
        self.tripToDepot = tripToDepot

        self.solutionDepots = np.zeros(shape = (nDepots, nTrips), dtype = int)  #Represents if a bus is going out of the depot to a trip. Initially has only zeros, and has binary values
        self.solutionTrips = np.zeros(shape = (nTrips, nTrips), dtype = int)    #Represents if a bus is going from a trip to another one.
        
        self.value = 0 
        
        self.listOfTripsPerBus = []
        

    def generateConstructiveSolution(self, seedSolution):
        random.seed(seedSolution)

        candidates = [n for n in range(self.nTrips)] #Candidates = list of trips that have not been visited yet by any bus!

        while(candidates != [])
            nextCandidate = candidates.pop(random.randint(0, len(candidates)))  #We get a random candidate from the list
            self.listOfTripsPerBus.append(ListBus(nextCandidate))
            
            
                costOfTripsFromActual = tripToTrip[actualTrip]
                reachableTrips = [n for n in costOfTripsFromActual if n > 0]
                minValue = -1

                while(reachableTrips != [] or minValue != -1):
                    if reachableTrips.index(min(reachableTrips)) in candidates:
                        minValue = min(reachableTrips)
                
                
                
                




            
            

        #Now, we need to check all the trips that we can get going from nextCandidate:
    

    def whichTripCanGo(self, actualTrip: int, candidates):
        """
        Returns the trip we will go next and the value we will increment in it
        Returns: (nextTrip: int, valueToIncrease: int)
        """
        costOfTripsFromActual = tripToTrip[actualTrip]



    



        
            