import sys, heapq

def solve():
    read = sys.stdin.readline
    H, W = map(int, read().split())
    num_list = [0] + list(map(int, read().split())) + [0]

    max_heap = []
    check = [True] * (W+2)

    for i in range(W+2):
        heapq.heappush(max_heap, (-num_list[i], i))

    left = (0, 0)
    right = (0, 0)
    for i in range(2):
        cost, index = heapq.heappop(max_heap)
        check[index] = False

        if index > right[1]:
            left = right
            right = (cost, index)

        elif index < right[1]:
            left = (cost, index)
    
    answer = 0
    for i in range(left[1]+1, right[1]):
        answer += min(-left[0], -right[0]) - num_list[i]
        check[i] = False

    while max_heap:
        cost, index = heapq.heappop(max_heap)

        if cost == 0:
            break

        if not check[index]:
            continue
        
        check[index] = False
        if index < left[1]:
            for i in range(index+1, left[1]):
                answer += min(-left[0], -cost) - num_list[i]
                check[i] = False
            
            left = (cost, index)

        else:
            for i in range(right[1]+1, index):
                answer += min(-right[0], -cost) - num_list[i]
                check[i] = False
            
            right = (cost, index)
    
    print(answer)


if __name__ == "__main__":
    solve()