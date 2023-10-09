from collections import deque


def solution(scoville, K):
    cnt = 0
    q = deque(sorted(scoville))
    mixed_q = deque()  # 섞은 결과 저장
    while (q and q[0] < K) or (mixed_q and mixed_q[0] < K):
        if len(q) + len(mixed_q) < 2:
            return -1
        cnt += 1
        tmp = [0] * 2
        for i in range(2):
            if q and mixed_q:
                if q[0] < mixed_q[0]:
                    tmp[i] = q.popleft()
                else:
                    tmp[i] = mixed_q.popleft()
            elif q:
                tmp[i] = q.popleft()
            else:
                tmp[i] = mixed_q.popleft()
        mixed_q.append(tmp[0] + tmp[1] * 2)
    return cnt
