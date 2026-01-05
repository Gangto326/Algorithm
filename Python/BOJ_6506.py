import sys

def solve():
    read = sys.stdin.readline

    while True:
        N, K = map(int, read().split())

        if N == 0 and K == 0:
            return
        
        num_list = list(map(int, read().split()))
        DP = [[0] * N for _ in range(K + 1)]

        for i in range(N):
            DP[1][i] = 1
        
        for length in range(2, K + 1):
            for i in range(N):
                for j in range(i):
                    if num_list[j] < num_list[i]:
                        DP[length][i] += DP[length - 1][j]
        
        print(sum(DP[K]))

if __name__ == "__main__":
    solve()