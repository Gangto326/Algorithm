import sys

def solve():
    N = int(sys.stdin.readline())

    DP = [0] * (N + 1)
    DP[0] = 1

    for i in range(2, N + 1):
        DP[i] += DP[i - 2] * 3

        for j in range(4, i + 1, 2):
            DP[i] += DP[i - j] * 2
    
    print(DP[-1])
    

if __name__ == "__main__":
    solve()