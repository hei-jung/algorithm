m, n = map(int, input().split())  # m: 가로 길이, n: 세로 길이
w = [0]  # 가로 자르는 점선
h = [0]  # 세로 자르는 점선
k = int(input())  # 점선 개수
for _ in range(k):
    way, idx = map(int, input().split())  # 방향, 번호
    if way == 1:  # 세로로 자르면 => 가로가 잘리게 됨
        w.append(idx)
    else:  # 가로로 자르면 => 세로가 잘리게 됨
        h.append(idx)
w = sorted(w) + [m]
h = sorted(h) + [n]
max_area = 0
for i in range(1, len(w)):
    for j in range(1, len(h)):
        area = (w[i] - w[i - 1]) * (h[j] - h[j - 1])
        if area > max_area:
            max_area = area
print(max_area)
