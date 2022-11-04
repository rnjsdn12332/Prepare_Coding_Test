def solution(board, skill):
    answer = 0
    zero_b=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for temp in skill :
        type_t, r1, c1, r2, c2, degree = temp
        #공격 스킬일 때
        if type_t==1 :
            val=-degree
        #회복 스킬일 때
        else :
            val=degree
        
        #누적합을 위한 값 설정
        zero_b[r1][c1]+=val
        zero_b[r2+1][c1]-=val
        zero_b[r1][c2+1]-=val
        zero_b[r2+1][c2+1]+=val

    
    #누적합 해주기
    for x in range(0,len(zero_b)-1) :
        #왼쪽에서 오른쪽으로 누적합
        for y in range(0, len(zero_b[0])-1) :
            zero_b[x+1][y]+=zero_b[x][y]
        #위에서 아래로 누적합
        for y2 in range(len(zero_b[0])-1) :
            zero_b[x][y2+1]+=zero_b[x][y2]
            #붕괴안된 건물 수 세기
            if board[x][y2]+zero_b[x][y2]>0 :
                answer+=1

    return answer
