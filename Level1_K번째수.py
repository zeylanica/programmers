https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    answer = []
    for i in range(0,len(commands)):
        temp = []
        front_idx = commands[i][0]
        end_idx = commands[i][1]
        val_idx = commands[i][2]
        temp = array[front_idx-1:end_idx]
        temp.sort()
        answer.append(temp[val_idx-1])
    return answer