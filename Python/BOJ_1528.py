import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = []
    num_queue = deque([4, 7])

    while num_queue:
        num = num_queue.popleft()
        
        if num <= 1000000:
            num_list.append(num)
            num_queue.append(num * 10 + 4)
            num_queue.append(num * 10 + 7)

    num_list.sort()

    BFS = deque()
    BFS.append((0, 0))
    check = [float('inf')] * (N + 1)
    check[0] = 0

    root = [float('inf')] * (N + 1)
    
    while BFS:
        n, count = BFS.popleft()

        if check[N] != float('inf'):
            break
        
        count += 1
        for num in num_list:
            next_n = n + num
            
            if next_n > N:
                break

            if check[next_n] > count:
                check[next_n] = count
                root[next_n] = n
                BFS.append((next_n, count))
        
    answer_list = []
    start = N

    if root[start] == float('inf'):
        print(-1)
        return

    while root[start] != float('inf'):
        answer_list.append(start- root[start])
        start = root[start]
    
    print(*sorted(answer_list))


if __name__ == "__main__":
    solve()