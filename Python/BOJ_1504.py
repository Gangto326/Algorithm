import sys, heapq

def solve():
    read = sys.stdin.readline
    N, E = map(int, read().split())

    node_list = [[] for _ in range(N+1)]
    for _ in range(E):
        left, right, cost = map(int, read().split())

        node_list[left].append((right, cost))
        node_list[right].append((left, cost))
    
    A, B = map(int, read().split())
    max_len = 200_000_000
    len_board = [[max_len, max_len], [max_len, max_len]]

    for i in range(2):
        heap = []
        check = [float('inf')] * (N+1)

        if i == 0:
            heapq.heappush(heap, (0, 1))
        else:
            heapq.heappush(heap, (0, N))

        while heap:
            total, node = heapq.heappop(heap)

            if node == A and len_board[i][0] == max_len:
                len_board[i][0] = total
            elif node == B and len_board[i][1] == max_len:
                len_board[i][1] = total
            
            if len_board[i][0] != max_len and len_board[i][1] != max_len:
                break

            for next, cost in node_list[node]:
                next_total = total + cost
                if check[next] > next_total:
                    check[next] = next_total
                    heapq.heappush(heap, (next_total, next))

    mid = max_len
    heap = []
    check = [float('inf')] * (N+1)
    heapq.heappush(heap, (0, A))

    while heap:
        total, node = heapq.heappop(heap)

        if node == B:
            mid = total
            break

        for next, cost in node_list[node]:
            next_total = total + cost
            if check[next] > next_total:
                check[next] = next_total
                heapq.heappush(heap, (next_total, next))

    AB = len_board[0][0] + len_board[1][1] + mid
    BA = len_board[0][1] + len_board[1][0] + mid

    if (len_board[0][0] == max_len or len_board[1][1] == max_len or mid == max_len) and (len_board[0][1] == max_len or len_board[1][0] == max_len or mid == max_len):
        print(-1)
    else:
        print(min(AB, BA))

if __name__ == "__main__":
    solve()