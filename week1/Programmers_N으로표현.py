#https://school.programmers.co.kr/learn/courses/30/lessons/42895
def solution(N, number):
    table=[[0]]
    #N이 포함하는 갯수
    for i in range(1, 9) :
        case=[]
        #N이 연달아 붙어 있는 갯수 예를들어 5가 3개일 때 55, 5 또는 5, 5, 5가 될 수 있는 것 처럼
        for j in range(1, i) :
            #
            for k in table[j] :
                #사칙연산 경우의 수 넣어주기
                for l in table[i-j] :
                    case.append(k+l)
                    if k>=l :
                        case.append(k-l)
                    case.append(k*l)
                    if k!=0 and l!=0 :
                        case.append(k//l)
        #단순히 숫자로만 구성되어있는 케이스 넣어주기
        case.append(int(str(N)*i))
        
        #케이스 안에 찾느 숫자가 있을 때 반환
        if number in case :
            return i
        #테이블에 case 배열 넣어주기
        table.append(list(set(case)))
    #8번까지 없을 떄 -1 반환
    return -1
