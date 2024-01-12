import sys
input = sys.stdin.readline

# 1.금메달 수가 더 많은 나라
# 2.금메달 수가 같으면, 은메달 수가 더 많은 나라
# 3.금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라
# 각 국가는 1부터 N 사이의 정수로 표현된다. 한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의된다.

n, k = map(int, input().split())
gold = [0]*(n+1)
silver = [0]*(n+1)
bronze = [0]*(n+1)
for _ in range(n):
    i, g, s, b = map(int, input().split())
    gold[i] = g
    silver[i] = s
    bronze[i] = b

ranking = 1
for i in range(1, n+1):
    if gold[i] > gold[k]:
        ranking += 1
    elif gold[i] == gold[k]:
        if silver[i] > silver[k]:
            ranking += 1
        elif silver[i] == silver[k]:
            if bronze[i] > bronze[k]:
                ranking += 1

print(ranking)
