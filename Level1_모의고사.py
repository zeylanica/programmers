#https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def solution(answers):
    answer = []
    sol1 = [1,2,3,4,5]
    sol2 = [2,1,2,3,2,4,2,5]
    sol3 = [3,3,1,1,2,2,4,4,5,5]
    sol1_cor = 0
    sol2_cor = 0
    sol3_cor = 0
    for i in range(0,len(answers)):
        if sol1[i%5] == answers[i] :
            sol1_cor = sol1_cor + 1
        if sol2[i%8] == answers[i] :
            sol2_cor = sol2_cor + 1
        if sol3[i%10] == answers[i] :
            sol3_cor = sol3_cor + 1
    if sol1_cor >= sol2_cor :
        if sol1_cor >= sol3_cor :
            answer.append(1)
    if sol2_cor >= sol1_cor :
        if sol2_cor >= sol3_cor :
            answer.append(2)
    if sol3_cor >= sol1_cor :
        if sol3_cor >= sol2_cor :
            answer.append(3)
    answer.sort()
            
    return answer