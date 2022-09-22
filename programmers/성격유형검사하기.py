def solution(survey, choices):
    """
    survey[i][0]: i+1번 질문의 비동의 관련 선택지
    survey[i][1]: i+1번 질문의 동의 관련 선택지
    choices[i]: 검사자가 선택한 i+1번째 질문 선택지
        - 1: survey[i][0] 3
        - 2: survey[i][0] 2
        - 3: survey[1][0] 1
        - 4: 0
        - 5: survey[i][1] 1
        - 6: survey[i][1] 2
        - 7: survey[i][1] 3
    """
    score_dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    types = list(score_dict.keys())

    answer = ''
    for i, choice in enumerate(choices):
        score = choice - 4
        if score < 0:
            score_dict[survey[i][0]] -= score
        else:
            score_dict[survey[i][1]] += score

    for i in range(1, 8, 2):
        answer += types[i] if score_dict[types[i]] > score_dict[types[i - 1]] else types[i - 1]

    return answer