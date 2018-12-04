set DEPOTS;
set TRIPS;
set N := (DEPOTS union TRIPS);

param maxbus{d in DEPOTS};
param M{i in N, j in N};

var x{k in DEPOTS, i in N, j in N}, >= 0, <= 1;

minimize cost: sum{k in DEPOTS, i in N, j in N} (x[k,i,j] * M[i,j]);

# Make sure only possible paths (M[i,j] != -1) are selected
s.t. POSSIBLE_PATHS {k in DEPOTS, i in N, j in N}: (x[k,i,j] * M[i,j]) >= 0;

# Maximum busses per depot
s.t. MAX_BUSSES {k in DEPOTS}: sum{j in TRIPS} x[k,k,j] <= maxbus[k];

# One bus for each trip
s.t. ALL_TRIPS {j in TRIPS}: sum{k in DEPOTS} x[k,k,j] + sum{k in DEPOTS, i in TRIPS} x[k,i,j] = 1;

# Make sure all paths are continuous and all busses return to depot
s.t. CONTINUOUS {k in DEPOTS, n in TRIPS}: sum{i in TRIPS} x[k,i,n] + x[k,k,n] = sum{j in TRIPS} x[k,n,j] + x[k,n,k];

end;
