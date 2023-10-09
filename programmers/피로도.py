answer = 0


def solution(k, dungeons):
    global answer
    n = len(dungeons)  # 던전의 개수
    visited = [0] * n

    def search(cnt, arr):
        global answer
        if cnt == n:
            tmp = k
            d_cnt = 0
            for idx in arr:
                if tmp < dungeons[idx][0]:
                    return
                tmp -= dungeons[idx][1]
                d_cnt += 1
                answer = max(answer, d_cnt)
            return
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                search(cnt + 1, arr + [i])
                visited[i] = 0

    search(0, [])
    return answer
