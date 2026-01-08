import sys

def solve():
    read = sys.stdin.readline

    N, M = map(int, read().split())
    num_list = list(map(int, read().split()))

    query_list = [0] * (N+1)
    for _ in range(M):
        start, end, cost = map(int, read().split())

        query_list[start-1] += cost
        query_list[end] -= cost

    for i in range(1, N):
        query_list[i] += query_list[i-1]
    
    for i in range(N):
        num_list[i] += query_list[i]
    
    print(*num_list)


if __name__ == "__main__":
    solve()