from math import sqrt

def solution(begin, end):
    MAX_VALUE = 10_000_000
    answer = [0] * (end - begin + 1)
    
    index = 0
    if begin == 1:
        begin += 1
        index += 1
    
    for num in range(begin, end + 1):
        start_num = int(sqrt(num))
        max_num = 1
        
        for i in range(2, start_num + 1):
            if not num % i:
                if num // i <= MAX_VALUE:
                    max_num = num // i
                    break

                else:
                    max_num = i
                    
        answer[index] = max_num
        index += 1
        
    return answer