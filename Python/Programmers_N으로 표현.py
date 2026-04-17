import heapq

def solution(N, number):
    num_list = []
    num = N
    num_list.append((N, 1))
    
    for i in range(2, 6):
        num *= 10
        num += N
        num_list.append((num, i))
    
    heap = []
    heapq.heappush(heap, (0, 0))
    check = {}
    check[0] = 0
    
    while heap:
        cost, num = heapq.heappop(heap)
        
        if check[num] < cost:
            continue
        
        if num == number:
            return cost
        
        for n, c in num_list:
            next_num = num + n
            next_cost = cost + c
            
            if next_cost > 8:
                break
            
            if next_num in check:
                if next_cost <= check[next_num]:
                    check[next_num] = next_cost
                    heapq.heappush(heap, (next_cost, next_num))
            else:
                check[next_num] = next_cost
                heapq.heappush(heap, (next_cost, next_num))
            
            next_num = num - n
            
            if next_num in check:
                if next_cost <= check[next_num]:
                    check[next_num] = next_cost
                    heapq.heappush(heap, (next_cost, next_num))
            else:
                check[next_num] = next_cost
                heapq.heappush(heap, (next_cost, next_num))
            
            next_num = num * n
            
            if next_num in check:
                if next_cost <= check[next_num]:
                    check[next_num] = next_cost
                    heapq.heappush(heap, (next_cost, next_num))
            else:
                check[next_num] = next_cost
                heapq.heappush(heap, (next_cost, next_num))
            
            next_num = num // n
            
            if next_num in check:
                if next_cost <= check[next_num]:
                    check[next_num] = next_cost
                    heapq.heappush(heap, (next_cost, next_num))
            else:
                check[next_num] = next_cost
                heapq.heappush(heap, (next_cost, next_num))
    
    return -1