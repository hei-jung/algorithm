from collections import deque

n, m = map(int, input().split())  # n: 사람의 수 / m: 파티의 수
truth = [0] * (n + 1)  # 진실을 아는 사람 리스트
tmp = list(map(int, input().split()))
if tmp == [0]:
    print(m)
    exit(0)
q = deque(tmp[1:])
for i in range(1, tmp[0] + 1):
    truth[tmp[i]] = 1

graph = [[] for _ in range(n + 1)]
party = [-1]  # party[i]: i번째 파티에 참석한 사람 리스트
for _ in range(m):
    tmp = list(map(int, input().split()))
    party.append(tmp[1:])
    for i in range(1, tmp[0] + 1):
        for j in range(i + 1, tmp[0] + 1):
            graph[tmp[i]].append(tmp[j])
            graph[tmp[j]].append(tmp[i])
graph = [list(set(x)) for x in graph]

while q:
    i = q.popleft()
    for ni in graph[i]:
        if truth[ni] == 0:
            q.append(ni)
            truth[ni] = 1

cnt = m
for i in range(1, m + 1):
    for j in party[i]:
        if truth[j] == 1:
            cnt -= 1
            break
print(cnt)
