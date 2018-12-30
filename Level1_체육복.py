#https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3#
def solution(n, lost, reserve):
    answer = n - len(lost)
    losted = []
    catched = []
    for i in reserve:
        if i in lost:
            losted.append(i)
    answer = answer + len(losted)
    for i in losted:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for i in reserve:
        if i-1 in lost and i-1 not in catched:
            catched.append(i-1)
            answer = answer + 1
        elif i+1 in lost and i+1 not in catched:
            catched.append(i+1)
            answer = answer + 1
    return answer