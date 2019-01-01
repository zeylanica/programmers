#https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3
def solution(arr, divisor):
    answer = []
    for idx in arr:
        if idx % divisor == 0:
            answer.append(idx)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer