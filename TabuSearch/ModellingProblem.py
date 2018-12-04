import numpy as np
import random
from operator import itemgetter

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
        self.numBus = maxBus
        
        self.depotToTrip = depotToTrip
        self.tripToTrip = tripToTrip
        self.tripToDepot = tripToDepot

        self.solutionDepots = np.zeros(shape = (nDepots, nTrips), dtype = int)  #Represents if a bus is going out of the depot to a trip. Initially has only zeros, and has binary values
        self.solutionTrips = np.zeros(shape = (nTrips, nTrips), dtype = int)    #Represents if a bus is going from a trip to another one.
        
        self.value = 0 
        
        self.listOfTripsPerBus = []
        

    def generateConstructiveSolution(self, seedSolution):
        random.seed(seedSolution)

        candidates = [0] * self.nTrips #Candidates = list of trips that have not been visited yet by any bus!
        nCandidates = self.nTrips

        while(nCandidates > 0):
            nextCandidate = random.randint(0, nCandidates-1)  #We get a random candidate from the list
            self.listOfTripsPerBus.append(ListBus(nextCandidate))
            nCandidates -= 1
            candidates[nextCandidate] = 1
            
            selectedDepot = self.selectDepot()

            self.listOfTripsPerBus[-1].insertNewDepot(selectedDepot)
            
            self.solutionDepots[selectedDepot][nextCandidate] = 1

            self.value += self.depotToTrip[selectedDepot][nextCandidate]
            
            endOfGraph = False
            while(not endOfGraph):
                allValuesCandidate = self.tripToTrip[nextCandidate]
                allValuesCandidate = transformListToTuple(allValuesCandidate)

                candidateCanAccess = [n for n in allValuesCandidate if n[0] > 0]
                notBeenChosen = [n for n in candidateCanAccess if candidates[n[1]] == 0]
                if(notBeenChosen == []):
                    self.value += self.tripToDepot[nextCandidate][selectedDepot]
                    endOfGraph = True
                
                else:
                    oldCandidate = nextCandidate
                    nextCandidate = random.randint(0,len(notBeenChosen)-1)
                    nextCandidate = notBeenChosen[nextCandidate][1]
                    self.listOfTripsPerBus[-1].insertNewTrip(nextCandidate)
                    nCandidates-=1
                    candidates[nextCandidate] = 1
                    self.value += self.tripToTrip[oldCandidate][nextCandidate]
    
    def selectDepot(self):
        selectedDepot = -1
        while(selectedDepot == -1):
            selectedDepot = random.randint(0, len(self.numBus)-1)
            if(self.numBus[selectedDepot] > 0):
                self.numBus[selectedDepot] -= 1
            else:
                if(max(self.numBus) == 0):
                    raise Exception("Problem: Not enough busses")
        return selectedDepot
    
    #------------------------------------------------------------------#

    def getNeighbor()


def transformListToTuple(listToTransform):
    newList = []
    for i in range(len(listToTransform)):
        newList.append((listToTransform[i], i))
    return newList
