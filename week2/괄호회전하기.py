#https://school.programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque
def reverse(char) :
    if char=="(" :
        return ")"
    elif char==")" :
        return "("
    elif char=="{" :
        return "}"
    elif char=="}" :
        return "{"
    elif char=="[" :
        return "]"
    elif dhar=="]" :
        return "["
def check(s) :

    q=deque(s)
    q2=deque()
    while q :
        temp=q.popleft()

        if temp in ["(","{","["] :
            q2.append(temp)
        else :
            if q2 :
                temp2=q2.pop()
                if not temp==reverse(temp2) :
                    q2.append(temp2)
    if q2 :
        return False
    else :
        return True

    
                
            
   
def solution(s):
    answer = 0
    cnt=0
    if s.count("{")==s.count("}") and s.count("(")==s.count(")") and s.count("[")==s.count("]"):
        q=deque(s)
        while q :
            if check(list(q)) :
                answer+=1

            q.append(q.popleft())
            cnt+=1
            
            if cnt>len(s)-1 :
                break
        
    return answer
