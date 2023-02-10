n = int(input())

a, b = 1, 3

for i in range(2, n + 1):
    a, b = b, b * 2 + a

print(b % 9901)
