import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    N = int(next(iterator))
    num_list = [int(next(iterator)) for _ in range(N)]
    DP = [1] * N

    for i in range(N-1, 0, -1):
        for j in range(i):
            if num_list[j] < num_list[i]:
                DP[j] = max(DP[j], DP[i] + 1)
    
    print(N - max(DP))


if __name__ == "__main__" :
    solve()