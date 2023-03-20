def solution(storey):
    answer = 0

    while storey:
        # a: 일의자리수, b: 십의자리수
        a, b = storey % 10, (storey // 10) % 10
        print('storey:', storey)
        if a > 5:
            answer += 10 - a
            storey += 10  # 올림
        elif a == 5:
            answer += 5
            storey += 10 if b >= 5 else 0
        else:
            answer += a
        storey //= 10
        print('count:', answer)

    return answer


storey = 75
ans = solution(storey)
print(ans)
