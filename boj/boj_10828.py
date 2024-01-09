import sys
input = sys.stdin.readline

stack = []
def run(op):
    if op[0] == "push":
        stack.append(op[1])
    elif op[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif op[0] == "size":
        print(len(stack))
    elif op[0] == "empty":
        print(0 if stack else 1)
    elif op[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)


for _ in range(int(input())):
    run(input().split())
