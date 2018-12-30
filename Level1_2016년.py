#https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
def solution(a, b):
    idxdays = 0
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    day31 = [1,3,5,7,8,10,12]
    day30 = [4,6,9,11]
    for i in range(0,a-1):
        if i+1 in day31:
            idxdays = idxdays + 31
        elif i+1 in day30:
            idxdays = idxdays + 30
        else:
            idxdays = idxdays + 29
    idxdays = idxdays + b
    idxdays = idxdays % 7
    answer = days[idxdays]
    return answer