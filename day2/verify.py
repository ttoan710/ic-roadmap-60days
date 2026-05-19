def logic(A,B):
    # return (A or B) and (A or not(B))
    return (A | B) & (A |(1-B))

for A in [0,1]:
    for B in [0,1]:
        print(A,B,logic(A,B))