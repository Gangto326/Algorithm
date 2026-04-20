from collections import deque

def solution(plans):
    for plan in plans:
        h, m = map(int, plan[1].split(":"))
        minute = h * 60 + m
        
        plan[1] = minute
        plan[2] = int(plan[2])
    
    plans.sort(key = lambda x: x[1])
    answer = []
    
    BFS = deque(plans)
    waiting = []
    time = 0
    
    while BFS:
        name, start, play = BFS.popleft()
        
        while start >= time and waiting:
            n, s, t = waiting.pop()
            time += t
            
            if time <= start:
                answer.append(n)
            
            else:
                over_time = time - start
                waiting.append([n, s, over_time])
                break
        
        time = start
        time += play
        
        if BFS and time > BFS[0][1]:
            over_time = time - BFS[0][1]
            play = over_time
            waiting.append([name, start, play])
            
        else:
            answer.append(name)
    
    while waiting:
        name, _, _ = waiting.pop()
        answer.append(name)
        
    
    return answer