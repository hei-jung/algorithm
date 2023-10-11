s = 0
max_s = 0
for _ in range(10):
    off, on = map(int, input().split())
    s -= off
    s += on
    if max_s < s:
        max_s = s

print(max_s)
