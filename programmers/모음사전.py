vowels = ['A', 'E', 'I', 'O', 'U']
answer = 0
idx = -1


def solution(word):
    def dfs(cnt, s):
        global answer, idx
        if cnt <= 5:
            idx += 1
            if s == word:
                answer = idx
        else:
            return
        for i in range(5):
            dfs(cnt + 1, s + vowels[i])

    dfs(0, '')

    return answer
