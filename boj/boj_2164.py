from collections import deque

n = int(input())
q = deque([i for i in range(1, n + 1)])
while len(q) > 1:
    q.popleft()  # 제일 위에 있는 카드 버리기
    x = q.popleft()
    q.append(x)  # 제일 위에 있는 카드 제일 밑으로
print(q.popleft())
