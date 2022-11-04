#https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    answer = 0
    graph=[[0] * (m + 1) for i in range(n + 1)]
    graph[1][1]=1
    for x in range(1, n+1) :
        for y in range(1, m+1) :
            if x==1 and y==1 :
                continue
            if [y,x] in puddles :
                graph[x][y]=0
            else :
                graph[x][y]=(graph[x - 1][y] + graph[x][y - 1])%1000000007

    return graph[n][m]
