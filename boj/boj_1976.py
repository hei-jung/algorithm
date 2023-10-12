# 유니온 파인드
# https://my-coding-notes.tistory.com/332
def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])
    return graph[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        graph[y] = x
    else:
        graph[x] = y


n, m = int(input()), int(input())
graph = [i for i in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            union(i, j)

graph = [0] + graph
path = list(map(int, input().split()))
start = graph[path[0]]
flag = 0
for i in range(1, m):
    if graph[path[i]] != start:
        flag = 1
        break
print(["YES", "NO"][flag])
