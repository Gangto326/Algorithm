def solution(name, yearning, photo):
    N = len(name)
    name_dict = {}
    
    for i in range(N):
        name_dict[name[i]] = yearning[i]
    
    answer = []
    for p in photo:
        total = 0
        
        for n in p:
            if n in name_dict:
                total += name_dict[n]
        
        answer.append(total)
    
    return answer