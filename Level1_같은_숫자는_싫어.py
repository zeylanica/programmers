#https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
def solution(arr):
    answer = []
    list_len = len(arr)
    idx = 0
    while idx < list_len-1:
        if arr[idx] == arr[idx+1]:
            idx = idx + 1
        else :
            answer.append(arr[idx])
            idx = idx + 1
    answer.append(arr[list_len-1])
    return answer

#for idx in arr:
#   if answer[-1:] == [idx] :
#       continue
#   answer.append(idx)
