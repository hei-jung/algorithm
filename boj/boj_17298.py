n = int(input())
A = list(map(int, input().split()))
arr = [-1] * n  # 정답 배열
stack = [0]  # 인덱스 비교
for i in range(1, n):
    while stack and A[i] > A[stack[-1]]:
        arr[stack.pop()] = A[i]
    stack.append(i)
print(*arr)
