import sys

n = int(sys.stdin.readline())  # 시험장 개수
a = list(map(int, sys.stdin.readline().split()))  # 각 시험장 응시자 수
# b: 총감독관이 감시할 수 있는 응시자 수 / c: 부감독관 "
b, c = map(int, sys.stdin.readline().split())

ans = 0
for i in range(n):
    a[i] = a[i] - b
    ans += 1
    if a[i] > 0:
        ans += a[i] // c if a[i] % c == 0 else a[i] // c + 1

print(ans)
