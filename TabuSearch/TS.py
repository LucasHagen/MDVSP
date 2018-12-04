import random
from ReadInstance import ReadInstance
from ModellingProblem import Solution

nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip = ReadInstance("./TabuSearch/instances-inp/m4n500s2.inp")


random.seed(5643877)

for i in range(1):
    try:
        test = Solution(nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip)
        test.generateConstructiveSolution()
        for j in range(1000):
            test.getNeighbor([])
            print(test.value)
            print(test.getNumOfBus())
    except Exception:
        test = None
