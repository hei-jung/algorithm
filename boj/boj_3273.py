import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())
is_a = [False] * 1000001  # a의 원소인지 여부
cnt = 0
for i in range(n):
    if 0 < x - a[i] <= 1000000 and is_a[x - a[i]]:
        cnt += 1
    is_a[a[i]] = True
print(cnt)
