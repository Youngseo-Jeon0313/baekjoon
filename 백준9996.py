N=int(input())

S,E = input().split("*")

P = []

for i in range(N):
    FN = str(input())

    if FN[:len(S)] == S and FN[-len(E):] ==E:
        P.append("DA")

    else:
        P.append("NE")

for i in range(N):
    print(P[i])