#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = participant[:]
    answer.sort()
    completion.sort()
    re_answer = ""
    flag_answer = 0 
    for i in range(0,len(completion)):
        if answer[i] != completion[i]:
            re_answer = answer[i]
            flag_answer = 1
            break
    if flag_answer == 0:
        re_answer = answer.pop()
    return re_answer