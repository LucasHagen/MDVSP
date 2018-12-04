import TS
from ReadInstance import ReadInstance
from ModellingProblem import Solution

nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip = ReadInstance("./TabuSearch/instances-inp/m4n500s2.inp")
#print(nDepots)
#print(nTrips)
#print(maxBus)
#print(depotToTrip)
#print(tripToTrip)
#print(tripToDepot)

test = Solution(nDepots, nTrips, maxBus, depotToTrip, tripToDepot, tripToTrip)
test.generateConstructiveSolution(12342)
print(test.value)
