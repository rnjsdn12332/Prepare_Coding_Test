
#https://school.programmers.co.kr/learn/courses/30/lessons/92342

from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    lion=[0 for _ in range(11)]
    comb = list(combinations_with_replacement(range(0, 11), n))
    maxgap=0
    for c in comb :
        lion=[0]*11
        a, l =0, 0
        for score in c :
            lion[10-score]+=1

        for i in range(11) :
            if info[i]<lion[i] :
                l+=(10-i)
            elif info[i]==lion[i]==0 :
                continue
            else :
                a+=(10-i)
        if l-a>0 :
            gap=l-a
            if gap>maxgap :
                maxgap=gap
                answer=lion
    return answer
