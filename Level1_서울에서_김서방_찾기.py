#https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3
def solution(seoul):
    for idx in range(0,len(seoul)):
        if(seoul[idx] is 'Kim'):
            return "김서방은 " + str(idx) + "에 있다"
    return answer