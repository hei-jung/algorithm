def solution(numbers, target):
    dp = [0]
    for i in range(len(numbers)):
        tmp = []
        for j in range(len(dp)):
            tmp.append(dp[j] + numbers[i])
            tmp.append(dp[j] - numbers[i])
        dp = tmp
    return dp.count(target)
