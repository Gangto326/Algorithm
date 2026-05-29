def solution(n, w, num):
    box_list = []
    
    for i in range(1, n + 1, w):
        row = list(range(i, min(i + w, n + 1)))
        
        if len(box_list) % 2 == 1:
            row.reverse()
            
        box_list.append(row)
        
    num_layer = -1
    target_col = -1
    
    for i in range(len(box_list)):
        for j in range(len(box_list[i])):
            if box_list[i][j] == num:
                num_layer = i
                
                if i % 2 == 0:
                    target_col = j
                    
                else:
                    target_col = w - len(box_list[i]) + j
                    
                break
                
        if num_layer != -1:
            break
            
    cnt = 0
    
    for i in range(num_layer, len(box_list)):
        
        if i % 2 == 0:
            if target_col < len(box_list[i]):
                cnt += 1
                
        else:
            if target_col >= w - len(box_list[i]):
                cnt += 1
                
    return cnt