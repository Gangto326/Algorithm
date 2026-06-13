import sys

def solve():
    MOD = 1_000_000_007
    N = int(sys.stdin.readline())

    DP = [0] * (N + 1)
    DP[0] = 1
    DP[1] = 1

    for i in range(2, N + 1):
        if i % 2 == 0:
            DP[i] = (DP[i - 1] + DP[i // 2]) % MOD
        
        else:
            DP[i] = DP[i - 1]
    
    print(DP[-1])


if __name__ == "__main__":
    solve()