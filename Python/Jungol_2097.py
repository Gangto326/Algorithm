import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [list(map(int, read().split())) for _ in range(N)]

    dijkstra = []
    heapq.heappush(dijkstra, (0, 0))

    check = [float('inf')] * (N + 1)
    check[0] = 0

    route = [i for i in range(N)]
    answer = 0
    while dijkstra:
        total, node = heapq.heappop(dijkstra)

        if node == M - 1:
            answer = total
            break

        if check[node] < total:
            continue

        for i in range(N):
            if i != node:
                next_total = total + board[node][i]

                if check[i] > next_total:
                    check[i] = next_total
                    heapq.heappush(dijkstra, (next_total, i))
                    route[i] = node
    
    print(answer)
    answer_list = []
    index = M - 1

    while True:
        answer_list.append(index + 1)

        if index == 0:
            break

        index = route[index]

    print(" ".join(map(str, reversed(answer_list))))


if __name__ == "__main__":
    solve()