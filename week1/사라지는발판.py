#https://school.programmers.co.kr/learn/courses/30/lessons/92345

#dfs 완전탐색 백트래킹 문제
#백트래킹과 minmax 알고리즘도 공부해보자

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]
#방문 체크 배열
visit=[[0]*5 for _ in range(5)]

#범위 확인 함수
def in_range(board, x, y):
    return x < 0 or x >= len(board[0]) or y < 0 or y >= len(board)

def move(board, x1, y1, x2, y2) :
        global vis
        #게임이 끝나서 이 판에서 질 경우
        if  visit[y1][x1]:
            return 0
        res=0
        
        
        for i in range(4) :
            tx=x1+dx[i]
            ty=y1+dy[i]
            if in_range(board, tx, ty) or board[ty][tx]==0 or visit[ty][tx] :
                continue
            
            #방문 체크
            visit[y1][x1]=1
            #돌아오는 턴 확인
            val=move(board, x2, y2, tx, ty)+1
            #방문 체크 해제
            visit[y1][x1]=0

            
            #res가 짝수이면 현재 턴의 플레이어가 승리, 홀수이면 패배
            
            #현재 패배하고 새로 계산된 승부에서 승리했을 때 
            if res%2==0 and val%2==1 : res=val
            #현재 패배하고 새로 계산된 승부에서 패배->max
            elif res%2==0 and val%2==0 : res=max(res, val)
            #현재 승리하고 새로 계산된 승부에서도 패배 ->min
            elif res%2==1 and val%2==1 : res=min(res, val)
            
        return res
            
def solution(board, aloc, bloc):
    return move(board, aloc[1], aloc[0], bloc[1], bloc[0])
