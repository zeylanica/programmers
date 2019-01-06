#https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
def solution(s):
    string = ""
    answer = sorted(s,key=str.lower, reverse=True)
    answer2 = []
    for idx in answer:
        if idx.isupper() :
            answer2.append(idx)
    for idx in answer2:
        if idx in answer:
            answer.remove(idx)
    answer2 = sorted(answer2, key=str.upper, reverse=True)
    answer.extend(answer2)
    for idx in answer:
        string = string + idx
    return string