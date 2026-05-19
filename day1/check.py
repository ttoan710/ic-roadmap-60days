def logic(A,B):
    return (A & B) | (1 - A)

for A in [0,1]:
    for B in [0,1]:
        print(A,B,logic(A,B))