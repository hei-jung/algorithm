"""2022 KAKAO BLIND RECRUITMENT"""
from math import ceil


def solution(fees, records):
    car_dict = {}  # {차량번호: 시간(분)}
    for record in list(map(lambda x: x.split(), records)):
        time = list(map(int, record[0].split(':')))
        # 출차
        if record[2] == "OUT":
            car_dict[record[1]] += time[0] * 60 + time[1]
        # 예전에 이미 한 번 입차 후 출차했던 차량이면
        if record[2] == "IN" and record[1] in car_dict:
            car_dict[record[1]] -= time[0] * 60 + time[1]
        # 아직 기록되지 않은 차량이 막 입차했다면
        if record[1] not in car_dict:
            car_dict[record[1]] = -time[0] * 60 - time[1]

    # 차량 번호가 작은 자동차부터 청구할 주차 요금
    answer = []
    for car in sorted(car_dict):
        if car_dict[car] <= 0:
            car_dict[car] += 1439  # 23*60+59

        # 요금: 기본요금 + 올림((이용시간 - 기본시간) / 단위시간) x 단위요금
        fee = fees[1] + ceil((car_dict[car] - fees[0]) / fees[2]) * fees[3]
        if fee <= fees[1]:
            answer.append(fees[1])
        else:
            answer.append(fee)

    return answer
