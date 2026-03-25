import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    edge_list = []

    for _ in range(M):
        start, end, cost = map(int, read().split())
        edge_list.append((start, end, cost))
    
    check = [float('inf')] * (N + 1)
    check[1] = 0
    for _ in range(N - 1):
        for start, end, cost in edge_list:
            if check[start] != float('inf') and check[end] > check[start] + cost:
                check[end] = check[start] + cost
    
    for start, end, cost in edge_list:
        if check[start] != float('inf') and check[end] > check[start] + cost:
            print(-1)
            return

    for i in range(2, N + 1):
        print(check[i] if check[i] != float('inf') else -1)


if __name__ == "__main__":
    solve()