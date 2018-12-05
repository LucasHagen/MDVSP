import time
import random
from ReadInstance import ReadInstance
from ModellingProblem import Solution

#"./TabuSearch/instances-inp/m4n1000s3.inp"
def runTabuSearch(dataPath, nTests, nNeighbors, seed):
    nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip = ReadInstance(dataPath)

    allBest = -1
    allBestBus = 0

    i = 0
    while(i < nTests):
        random.seed(seed)
        seed += 1
        execTime = time.time()
        try:
            #execTime = time.time()
            minimalValue = 999999999999999999
            tabuList = []
            best = Solution(nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip)
            best.generateConstructiveSolution()

            print("{}".format(i), end='    ')
            print("{}".format(best.value), end='    ')

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

                #print(best.value)
                #print(best.getNumOfBus())

            if allBest == -1 or allBest > best.value:
                allBest = best.value
                allBestBus = best.getNumOfBus()


            print("{}".format(best.value), end='    ')
            print("{0:.2f}".format(time.time() - execTime))
            i+=1

        except Exception:
            test = None

    print("Best Solution: {}, with {} busses".format(allBest, allBestBus))
