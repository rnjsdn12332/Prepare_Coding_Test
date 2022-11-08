#https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    for num in range(left, right+1) :
        col=num//n
        row=num%n
        answer.append(max(col, row)+1)
    return answer
    
