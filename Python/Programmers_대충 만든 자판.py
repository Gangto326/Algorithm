def solution(keymap, targets):
    key_dict = {}
    answer = []
    
    for key in keymap:
        for i, v in enumerate(key):
            if not v in key_dict:
                key_dict[v] = i + 1
            else:
                key_dict[v] = min(key_dict[v], i + 1)
            
    for target in targets:
        total = 0
        
        for n in target:
            if n in key_dict:
                total += key_dict[n]
            else:
                total = -1
                break
        
        answer.append(total)
    
    return answer