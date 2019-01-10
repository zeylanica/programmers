#https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3
def solution(s):
    answer = True
    if(len(s) == 4 or len(s) == 6):
        for idx in s:
            if(idx.isdigit() == False):
                answer = False
                break
    else:
        answer = False
    return answer