import sys

n = int(sys.stdin.readline())  # 스위치 개수
switch = [-1] + list(map(int, sys.stdin.readline().split()))  # 스위치


def switch1(num):
    for i in range(1, n + 1):
        if i % num == 0:
            switch[i] = int(not switch[i])


def switch2(num):
    switch[num] = int(not switch[num])  # 기준 스위치 상태 변경
    for i in range(1, num):
        if num - i < 1 or num + i > n or switch[num - i] != switch[num + i]:
            return
        switch[num - i] = int(not switch[num - i])
        switch[num + i] = int(not switch[num + i])


t = int(sys.stdin.readline())  # 학생 수
for _ in range(t):
    student, num = map(int, sys.stdin.readline().split())  # 성별, 숫자
    if student == 1:
        switch1(num)
    elif student == 2:
        switch2(num)

for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
