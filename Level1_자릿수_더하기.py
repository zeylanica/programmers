#https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3
def solution(n):
    answer = 0
    for idx in str(n):
        answer = answer + int(idx)
    return answer