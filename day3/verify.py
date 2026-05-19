def half_adder(A, B):
    return A ^ B, A & B;

for A in [0,1]:
    for B in [0,1]:
        print(A,B,half_adder(A,B))