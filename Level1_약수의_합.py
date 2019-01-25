#https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3
def solution(n):
    arr = []
    answer = 0
    for idx in range(1,n+1):
        if n % idx == 0:
            arr.append(idx)
    for idx in arr:
        answer = answer + idx
    return answer