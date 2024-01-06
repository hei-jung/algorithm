import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(input()[:n])

stack = []
cnt = k  # 지울 숫자의 개수
for i in range(n):
    while cnt > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        cnt -= 1
    stack.append(num[i])

print(''.join(stack[:n-k]))
