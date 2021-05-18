N = int(input())
P = [0, 1, 1]
for i in range(3, N + 1):
    P.append(P[i - 3] + P[i - 2])
print(P[N])
