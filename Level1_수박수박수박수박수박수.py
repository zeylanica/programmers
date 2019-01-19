#https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3
def solution(n):
    string = "수박"
    if(n % 2 == 0):
        answer = string * (n//2)
    else:
        answer = string * (n//2+1)
        answer = answer[0:-1]

    return answer