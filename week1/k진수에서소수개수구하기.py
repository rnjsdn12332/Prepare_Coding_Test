#https://school.programmers.co.kr/learn/courses/30/lessons/92335

from collections import deque
def solution(n, k):
    #소수 카운트하는 변수
    cnt=0
    
    #진수 변환 후 숫자 넣을 큐
    q=deque()
    
    #진수 변환
    while n!=0 :
        q.appendleft(str(n%k))
        n=n//k
    
    #큐를 문자열로 변환
    trans=''
    trans=trans.join(q)

    #split을 사용하여 분리
    array=trans.split('0')

    #소수 찾는 함수
    def find_sosu(x) :
        if x==1 :
            return False
        if x==2 :
            return True
        for i in range(2, int(x**(0.5))+1) :
            if x%i==0 :
                return False
        return True
   
    for val in array :
        if not val=='' :
            if find_sosu(int(val)) :
                cnt+=1
    
    return cnt
