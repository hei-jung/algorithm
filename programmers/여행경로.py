def solution(tickets):
    answer = []
    n = len(tickets)
    visited = [0] * n

    def dfs(a, path, cnt):
        if cnt == n:
            answer.append(path)
            return
        for i, (dep, arr) in enumerate(tickets):
            if a == dep and visited[i] != 1:
                visited[i] = 1
                dfs(arr, path + [arr], cnt + 1)
                visited[i] = 0

    dfs("ICN", ["ICN"], 0)
    return min(answer)
