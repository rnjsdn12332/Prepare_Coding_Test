
#스트라이크, 볼 갯수 계산하는 함수
def play(robot, user) :
    cnt=[0,0]
    for i in range(3) :
        if robot[i]==user[i] :
            cnt[1]+=1
        else :
            if user[i] in robot :
                cnt[0]+=1
    return cnt

#볼, 스트라이크 유무 결과 확인
def result(cnt) :
    if 0 in cnt :
        if cnt[0]!=0 :
            return 1
        elif cnt[1]!=0 :
            return 2
        else :
            return 0
    else :
        return 3
        
#결과에 맞게 print하는 함수
def print_result(cnt, check) :
    if check==0 :
        print("낫싱")
    elif check==1 :
        print(str(cnt[0])+"볼")
    elif check==2:
        print(str(cnt[1])+"스트라이크")
    elif check==3 :
        print(str(cnt[0])+"볼 "+str(cnt[1])+"스트라이크")    

print("숫자 야구 게임을 시작합니다.")
robot="425"
while True :
    user=input("숫자를 입력해주세요 : ")
    cnt=play(robot, user)
    check=result(cnt)
    print_result(cnt, check)
    if cnt[1]==3 :
        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
        break
