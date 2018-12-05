set DEPOTS;
set TRIPS;

set ALL := DEPOTS union TRIPS;

param M{ALL,ALL};

set V{k in DEPOTS} := {k} union TRIPS;

set A{k in DEPOTS} within {ALL,ALL} :=
          setof{j in TRIPS : M[k,j] > 0} (k,j) union
          setof{i in TRIPS : M[i,k] > 0} (i,k) union
          setof{i in TRIPS, j in TRIPS : M[i,j] > 0} (i,j);

param maxbus{k in DEPOTS};

# If is used
var X{k in DEPOTS,(i,j) in A[k]}, >= 0, <= 1;

minimize cost: sum{k in DEPOTS, (i,j) in A[k]} X[k,i,j] * M[i,j];

s.t. ALL_TRIPS {j in TRIPS}: sum{k in DEPOTS, (i,j) in A[k]} X[k,i,j] = 1;

s.t. MAX_BUS {k in DEPOTS}: sum{(k,j) in A[k]} X[k,k,j] <= maxbus[k];

s.t. FLOW {k in DEPOTS, v in V[k]}:
    sum{(i,v) in A[k]} X[k,i,v] =
    sum{(v,j) in A[k]} X[k,v,j];

end;