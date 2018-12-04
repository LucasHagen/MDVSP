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
        self.numBus = [n for n in maxBus]
        self.maxBus = [n for n in maxBus]

        self.depotToTrip = depotToTrip
        self.tripToTrip = tripToTrip
        self.tripToDepot = tripToDepot
        
        self.value = 0 
        
        self.listOfTripsPerBus = []

    def generateConstructiveSolution(self):
        print("Generating new solution:")

        candidates = [0] * self.nTrips #Candidates = list of trips that have not been visited yet by any bus!
        nCandidates = self.nTrips

        while(nCandidates > 0):
            nextCandidate = random.randint(0, nCandidates-1)  #We get a random candidate from the list
            self.listOfTripsPerBus.append(ListBus(nextCandidate))
            nCandidates -= 1
            candidates[nextCandidate] = 1
            
            selectedDepot = self.selectDepot()

            self.listOfTripsPerBus[-1].insertNewDepot(selectedDepot)
            
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
                    print("Error creating instance, creating another instead")
                    raise Exception("Problem: Not enough busses")
        return selectedDepot
    
    def getNumOfBus(self):
        return((sum(self.maxBus) - sum(self.numBus)))
    
    #------------------------------------------------------------------#

    def getNeighbor(self, tabuList: list):
        if (random.randint(0, 100) > 96):
            changePath = random.randint(0, len(self.listOfTripsPerBus)-1)
            changeDepot = -1
            while(changeDepot < 0):
                checkDepot = random.randint(0, self.nDepots-1)
                if(checkDepot != self.listOfTripsPerBus[changeDepot].depot):
                    changeDepot = checkDepot
                    oldDepot = self.listOfTripsPerBus[changePath].depot
                    firstOfPath = self.listOfTripsPerBus[changePath].path[0]
                    lastOfPath = self.listOfTripsPerBus[changePath].path[-1]
                    
                    self.value -= self.depotToTrip[oldDepot][firstOfPath]
                    self.value -= self.tripToDepot[lastOfPath][oldDepot]
                    self.value += self.depotToTrip[changeDepot][firstOfPath]
                    self.value += self.tripToDepot[lastOfPath][changeDepot]
                    
                    self.listOfTripsPerBus[changeDepot].insertNewDepot(changeDepot)
        
        validPathToChange = False
        while(not validPathToChange):
            changePath = random.randint(0, len(self.listOfTripsPerBus)-1)

            changeTripIndex = random.randint(0, len(self.listOfTripsPerBus[changePath].path)-1)
            
            while(self.listOfTripsPerBus[changePath].path[changeTripIndex] in tabuList):
                changeTripIndex = random.randint(0, len(self.listOfTripsPerBus[changePath].path)-1)
            
            if (changeTripIndex == 0):   #Special case
                pass
            elif (changeTripIndex == len(self.listOfTripsPerBus[changePath].path)-1):  #Special case
                pass
            else:

                beforeToChange = self.listOfTripsPerBus[changePath].path[changeTripIndex-1]
                afterToChange = self.listOfTripsPerBus[changePath].path[changeTripIndex+1]
                changeTrip = self.listOfTripsPerBus[changePath].path[changeTripIndex]

                if(self.tripToTrip[beforeToChange][afterToChange] > 0):

                    possiblePaths = []
                    for i in range(len(self.listOfTripsPerBus)):
                        if(self.tripToTrip[self.listOfTripsPerBus[i].path[-1]][changeTrip] > 0):
                            possiblePaths.append(i)        
                    if(possiblePaths != []):
                        newPath = random.randint(0, len(possiblePaths)-1)
                        newPath = possiblePaths[newPath]
                            
                        self.value += self.tripToTrip[self.listOfTripsPerBus[newPath].path[-1]][changeTrip]
                        self.value -= self.tripToDepot[self.listOfTripsPerBus[newPath].path[-1]][self.listOfTripsPerBus[newPath].depot]
                        self.value += self.tripToDepot[changeTrip][self.listOfTripsPerBus[newPath].depot]
                        self.listOfTripsPerBus[changePath].path.pop(changeTripIndex)
                        self.listOfTripsPerBus[newPath].insertNewTrip(changeTrip)
                            

                        self.value -= self.tripToTrip[changeTrip][afterToChange]
                        self.value -= self.tripToTrip[beforeToChange][changeTrip]
                        self.value += self.tripToTrip[beforeToChange][afterToChange]
                        validPathToChange = True
        return changeTrip

                    



def transformListToTuple(listToTransform):
    newList = []
    for i in range(len(listToTransform)):
        newList.append((listToTransform[i], i))
    return newList
