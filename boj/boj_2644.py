from collections import deque

n = int(input())  # 전체 사람의 수
person1, person2 = map(int, input().split())  # 촌수 계산할 두 사람
graph = [[] for _ in range(n + 1)]

m = int(input())  # 부모-자식 관계 수
for _ in range(m):
    x, y = map(int, input().split())  # x: 부모 / y: 자식
    graph[y].append(x)
    graph[x].append(y)


def bfs(a, b):
    visited = [0] * (n + 1)  # a 기준 촌수 계산
    q = deque([a])
    visited[a] = 0
    while q:
        c = q.popleft()
        if c == b:
            print(visited[b])
            exit(0)
        for p in graph[c]:
            if visited[p] == 0:
                q.append(p)
                visited[p] = visited[c] + 1
    return -1


print(bfs(person1, person2))
