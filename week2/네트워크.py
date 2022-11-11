#https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visit=['0']*n
    def dfs(i,visit,computers, network) :
        visit[i]=str(network)
        for j in range(n) :
            if visit[j]=='0':
                if computers[i][j]==1 :
                    dfs(j,visit,computers,network)

    network=1
    while True :
        if '0' in visit :
            x=visit.index('0')
            print(x)
            dfs(x,visit, computers, network)
            network+=1
        else :
            break
    
    return int(max(visit))
