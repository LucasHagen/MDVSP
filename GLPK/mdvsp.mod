set DEPOTS;
set TRAVELS;
set N := (DEPOTS union TRAVELS);

param maxbus{d in DEPOTS};
param M{i in N, j in N};

var x{k in DEPOTS, i in N, j in N} binary;

minimize cost: sum{k in DEPOTS, i in N, j in N} (x[k,i,j] * M[i,j]);

# Make sure only possible paths (M[i,j] != -1) are selected
s.t. POSSIBLE_PATHS {k in DEPOTS, i in N, j in N}: (x[k,i,j] * M[i,j]) >= 0;

# Maximum busses per depot
s.t. MAX_BUSSES {k in DEPOTS}: sum{j in TRAVELS} x[k,k,j] <= maxbus[k];

# One bus for each travel
s.t. ALL_TRAVELS {j in TRAVELS}: sum{k in DEPOTS} x[k,k,j] + sum{k in DEPOTS, i in TRAVELS} x[k,i,j] = 1;

# Make sure all paths are continuous and all busses return to depot
s.t. CONTINUOUS {k in DEPOTS, n in TRAVELS}: sum{i in TRAVELS} x[k,i,n] + x[k,k,n] = sum{j in TRAVELS} x[k,n,j] + x[k,n,k];

end;
