import sys

n = int(sys.stdin.readline())
a, b = 0, 1
for _ in range(2, n + 1):
    a, b = b, a + b
print(b)
