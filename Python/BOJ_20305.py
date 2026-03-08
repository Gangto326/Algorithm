import sys

def solve():
    MOD = 1_000_000_007
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    Q = int(next(iterator))

    pibo = [0] * (N + 3)
    pibo[1] = 1
    for i in range(2, N + 3):
        pibo[i] = (pibo[i - 1] + pibo[i - 2]) % MOD
    
    DP = [0] * (N + 3)
    for _ in range(Q):
        start, end = int(next(iterator)), int(next(iterator))
        DP[start] = (DP[start] + 1) % MOD
        DP[end + 1] = (DP[end + 1] - pibo[end - start + 2]) % MOD
        DP[end + 2] = (DP[end + 2] - pibo[end - start + 1]) % MOD
    
    answer = [0] * (N + 3)
    answer[1] = DP[1] % MOD
    for i in range(2, N + 3):
        answer[i] = (DP[i] + answer[i - 1] + answer[i - 2]) % MOD

    print(*answer[1:-2])


if __name__ == "__main__":
    solve()