import random
from ReadInstance import ReadInstance
from ModellingProblem import Solution

nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip = ReadInstance("./TabuSearch/instances-inp/m4n1000s3.inp")

nTests = 5
nNeighbors = 5
random.seed(564387)

i = 0
while(i < nTests):
    try:
        minimalValue = 999999999999999999
        tabuList = []
        best = Solution(nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip)
        best.generateConstructiveSolution()
        
        tabu = [0] * nNeighbors
        clone = [0] * nNeighbors
        iterationValues = [0] * nNeighbors

        for j in range(1000):
            bestChanged = False
            for k in range(nNeighbors):
                clone[k] = best.cloneSolution()
                tabu[k] = clone[k].getNeighbor(tabuList)
                iterationValues[k] = clone[k].value

            if(min(iterationValues) < minimalValue):
                newBestIndex = iterationValues.index(min(iterationValues))
                best = clone[newBestIndex]
                bestChanged = True
            
            #if(bestChanged):
                #tabuList.append(tabu[newBestIndex])

            if(j > 20 and len(tabuList) > 0):
                tabuList.pop(0)
            
            print(best.value)
            print(best.getNumOfBus())
        
        print("BEST OF ITERATION: -------------------")
        print(best.value)
        print(best.getNumOfBus())
        print()
        i+=1

    except Exception:
        test = None
