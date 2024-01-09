import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

idx = 0
stack = []
op = []
for i in range(1, n+1):
    stack.append(i)
    op.append("+")
    while stack and stack[-1] == arr[idx]:
        stack.pop()
        op.append("-")
        idx += 1

# arr와 똑같은 수열을 만들 수 있다면 stack이 빈 상태일 것.
if stack:
    print("NO")
else:
    print("\n".join(op))
