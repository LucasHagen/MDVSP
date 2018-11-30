set K;
set T;

set ALL := K union T;

set V{k in K} := {k} union T;

set TARC within {ALL,ALL};

set KARC{k in K} within {ALL,ALL};

set A{k in K} within {ALL,ALL} := KARC[k] union TARC;

param M{ALL,ALL};

param MAX{k in K};

var X{k in K,(i,j) in A[k]} binary;

minimize cost: sum{k in K, (i,j) in A[k]} X[k,i,j] * M[i,j];

s.t. ALL_TRIPS {i in T}: sum{k in K, (i,j) in A[k]} X[k,i,j] = 1;

s.t. MAX_BUS {k in K}: sum{(k,j) in A[k]} X[k,k,j] <= MAX[k];

s.t. FLOW {k in K, i in (V[k] diff {k})}:
    sum{(j,i) in A[k]} X[k,j,i] =
    sum{(i,j) in A[k]} X[k,i,j];

printf: "V:\n";
printf{k in K, v in V[k]}: " [%s] %s\n", k, v;
printf: "A:\n";
printf{k in K, (i,j) in A[k]}: "[%s] %s -> %s\n", k, i, j;

data;

set K := D1 D2;

set T := T1 T2;

set TARC := (T1, T2);

set KARC[D1] := (D1, T1) (T1, D1);
set KARC[D2] := D2 T2 T2 D2;

param MAX := D1 1 D2 1;

param M :     D1    D2    T1    T2 :=
        D1    0     0     1     0
        D2    0     10    0     2
        T1    2     0     0     0
        T2    0     2     0     0;

end;
