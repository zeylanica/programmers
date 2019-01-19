#https://programmers.co.kr/learn/courses/30/lessons/12925?language=python3
def solution(n):
    if(n[0] == '+'):
        return int(n[1:])
    else:
        return int(n[0:])