#https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3
def solution(a, b):
    answer = 0
    if a > b :
        a , b = b , a
    answer = sum(range(a,b+1))
    return answer