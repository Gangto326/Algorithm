def solution(schedules, timelogs, startday):
    answer = 0
    
    
    def calculate(t):
        if t % 100 >= 50:
            return (t // 100 + 1) * 100 + t % 10
        else:
            return t + 10
        
    
    for i in range(len(timelogs)):
        cnt = 0
        day = startday

        for j in range(7):
            if day <= 5:
                time = calculate(schedules[i])

                if time >= timelogs[i][j]:
                    cnt += 1
                
                day += 1

            else:
                if day == 7:
                    day = 1
                    
                else:
                    day = 7

        if cnt == 5:
            answer += 1

    return answer