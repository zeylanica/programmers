#https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3
def solution(arr):
    if(len(arr) == 1):
        return [-1]
    min = arr[0]
    for idx in arr:
        if(min > idx):
            min = idx
    arr.remove(min)
    return arr