#https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
def solution(s):
    answer = ''
    idx = len(s) // 2
    cp = len(s) % 2
    if cp == 1:
        answer = s[idx]
    else :
        answer = s[idx - 1] + s[idx]
    return answer