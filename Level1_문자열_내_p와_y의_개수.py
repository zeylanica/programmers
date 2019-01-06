#https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3
def solution(s):
    Ppint = 0
    Yyint = 0
    for idx in s:
        if(idx ==  'p' or idx ==  'P'):
            Ppint = Ppint + 1
        if(idx ==  'Y' or  idx == 'y' ):
            Yyint = Yyint + 1
    if Ppint == Yyint:
        return True
    else :
        return False

#count 함수, s.lower() 를 사용할 수 있음.