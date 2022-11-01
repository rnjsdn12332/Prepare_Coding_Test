from collections import deque
import math
def solution(fees, records):
    answer = []
    
    #기준 시간 요금제 변수 저장
    p_time, p_fee, m_time,m_fee=fees
    
    #차 가격 등록 사전
    car_fee=dict()
    #차 이용시간 등록 사전
    car_record=dict()
    #차 시작시간 업데이트 사전
    car_check=dict()
    #차 입출 기록 등록 사전
    car_inorout=dict()

    
    
    for record in records :
        real_time, car_number, in_or_out=record.split(" ")
        
        #분 단위로 시간 환산
        h, m=real_time.split(':')
        time=int(h)*60+int(m)

        #입차한 기록일 경우
        if in_or_out=="IN" :
            #차 시작시간 업데이트
            car_check[car_number]=time
            #입출차 기록에 입차로 저장
            car_inorout[car_number]="IN"
        #출차 기록일 경우
        else :
            #차 이용시간 등록 사전에 차가 등록되지않은 경우->입출차 계산한 이용시간 등록
            if not car_number in car_record.keys() :
                car_record[car_number]=time-car_check[car_number]
            #등록사전에 차가 등록된 경우는 이용시간 추가
            else :
                car_record[car_number]+=(time-car_check[car_number])
            #차 입출차 기록 사전에 출차로 등록
            car_inorout[car_number]="OUT"
    
    #이용요금 게산 함수
    def carculate_fee(time) :
        #기본 시간 초과한 경우
        if time>=p_time :   
            return p_fee+math.ceil((time-p_time)/m_time)*m_fee
        #기본 시간 내에 이요한 경우
        else :
            return p_fee
    
    #출차가 등록되지 않은 경우 이용시간 등록 및 업데이트
    for car_num, time in car_check.items() :
        if car_inorout[car_num]=="IN" :
            h, m="23:59".split(':')
            out_time=int(h)*60+int(m)
            time=out_time-car_check[car_num]
            if car_num in car_record.keys() :
                car_record[car_num]+=time
            else :
                car_record[car_num]=time

    
    #차 이용시간으로 총 게산 요금 등록
    for car_num, time in car_record.items() :
        fee=carculate_fee(time)
        car_fee[car_num]=fee
    
    #차 이용요금 사전을 리스트로 변환 후 정렬
    result=list(car_fee.items())
    result.sort(key=lambda x:x[0])
    
    #결과 배열에 저장
    for res in result :
        answer.append(res[1])
    return answer
