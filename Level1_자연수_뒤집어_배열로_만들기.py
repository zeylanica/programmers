#https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
def solution(n):
    answer = []
    for idx in str(n):
        answer.append(int(idx))
    answer.reverse()
    return answer