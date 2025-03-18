def solution(storey):
    answer = 0
    div = 10
    while storey>0:
        #print(storey)
        if storey%div>5:
            #더해
            answer+=10-(storey%div)
            storey+=10-(storey%div)
        elif storey%div==5:
            if storey>div and (storey//10)%10 > 4:
                answer+=10-(storey%div)
                storey+=10-(storey%div)
            else:
                answer+=storey%div
                storey-=(storey%div)
        else:
            answer+=storey%div
            storey-=(storey%div)
            
        storey//=div
        
            
    return answer