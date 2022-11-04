def solution(info, edges):
    answer = 0
    #방문 노드 확인 배열
    visit=[0]*len(info) 
    #루트 노드는 무조건 양이기에 0의 위치에 양을 표현하는 1을 저장
    visit[0]=1
    #양이 몇마린지 저장할 배열
    sheep_array=[]

    
    def dfs(sheep, wolf) :
        
        #양의 수가 늑대의 수보다 클 경우 양의 수 넣는 배열에 저장
        if sheep>wolf :
            sheep_array.append(sheep)

        #아닐 경우 함수 반환
        else :

            return 
        
        #주어진 엣지를 다 돌아본다
        for edge in edges :
            #부모와 자식 노드 변수 저장
            parent=edge[0]
            child=edge[1]
            #부모노드는 방문했으나, 자식 노드가 방문되지 않았을 경우
            if visit[parent]!=0 and visit[child]==0 :
                #자식 노드 방문 처리
                visit[child]=1
                #자식 노드가 양인지 늑대인지 확인 후 dfs
                if info[child]==0:  
                    dfs(sheep+1, wolf)
                else :
                    dfs(sheep, wolf+1)
                #다시 자식 노드의 방문을 해제해줌 
                #why?-dfs 다 끝났을때는 그 노드에서 갈수 있는 모든 노드를 방문했거나 늑대의 수가 양의 수보다 많아서 return했을 경우이므로 다른 경로를 찾기 위해 방문 해제해줘야함
                
                visit[child]=0
    
    #dfs 호출 루트노드는 무조건 양 한 마리기 때문에 1, 0을 넣어줌
    dfs(1,0)   
    print(sheep_array)
    
    #배열 중 최댓값 반환!
    return max(sheep_array)
