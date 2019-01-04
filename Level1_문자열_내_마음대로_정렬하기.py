#https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3
def solution(answer, n):
    answer.sort()
    mindex = 0
    temp = 0
    for idx in range(1,len(answer)):
        mindex = idx-1
        temp = answer[idx]
        while(answer[mindex][n] > temp[n] and mindex >=0) :
            answer[mindex+1] = answer[mindex]
            mindex = mindex - 1
        answer[mindex + 1] = temp
    return answer

# def s_sort(strings, n):
#     return sorted(strings, key = lambda x: x[n])