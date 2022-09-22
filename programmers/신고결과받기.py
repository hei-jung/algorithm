"""2022 KAKAO BLIND RECRUITMENT"""
from collections import Counter


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    id_dict = {id: [] for id in id_list}  # {신고한유저: [신고된유저]}
    reported = Counter()  # {신고된유저: 신고된횟수}
    for ids in list(map(lambda x: x.split(), report)):
        if ids[1] not in id_dict[ids[0]]:
            id_dict[ids[0]].append(ids[1])
            reported[ids[1]] += 1

    # 신고횟수가 정지기준을 넘어가는 경우만 세기
    for i, user_id in enumerate(id_dict):
        for report_id in id_dict[user_id]:
            if reported[report_id] >= k:
                answer[i] += 1

    return answer
