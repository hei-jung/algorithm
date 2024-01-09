import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))