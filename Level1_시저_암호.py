#https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3
def solution(s, n):
    answer = ""
    stringlower = "abcdefghijklmnopqrstuvwxyz"
    stringupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for idx in s :
        if idx == ' ':
            answer = answer + idx
        elif idx in stringlower:
            temp = ord(idx) + n
            if temp > 122:
                temp = temp - 26
            answer = answer + chr(temp)
        else :
            temp = ord(idx) + n
            if temp > 90:
                temp = temp - 26
            answer = answer + chr(temp)
    return answer