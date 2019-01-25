#https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3
def solution(s):
    flag = 1;
    answer = ""
    for idx in s:
        if(idx == ' '):
            flag = 1
            answer = answer + ' '
        elif(flag == 1):
            flag = 0
            answer = answer + idx.upper()
        else:
            flag = 1
            answer = answer + idx.lower()
    return answer