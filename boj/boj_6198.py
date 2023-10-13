import sys

input = sys.stdin.readline

n = int(input())
heights = []
for i in range(n):
    heights.append(int(input()))

s = 0
stack = []
for h in heights:
    while stack and h >= stack[-1]:
        stack.pop()
    stack.append(h)
    s += len(stack) - 1
print(s)
