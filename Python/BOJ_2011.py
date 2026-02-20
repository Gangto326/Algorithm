import sys

def solve():
    MOD = 1_000_000
    password = list(sys.stdin.readline().strip())
    N = len(password)

    if N == 0 or password[0] == "0":
        print(0)
        return

    DP = [0] * (N+1)
    DP[0] = 1
    DP[1] = 1

    for i in range(2, N+1):
        if int(password[i-1]):
            DP[i] += DP[i-1]
        
        disit = int(password[i-2]) * 10 + int(password[i-1])
        if 10 <= disit <= 26:
            DP[i] += DP[i-2]
        
        DP[-1] %= MOD
    
    print(DP[-1])
    

if __name__ == "__main__":
    solve()