import sys

def solve():
    MOD = 1_000_000
    password = list(map(int, list(sys.stdin.readline().strip())))
    DP = [[0] * 27 for _ in range(len(password))]
    DP[0][password[0]] = 1

    if not password[0]:
        print(0)
        return
    
    if len(password) >= 2:
        sum_num = password[0] * 10 + password[1]
        DP[1][password[1]] = 1 if password[1] else 0

        if 0 < sum_num <= 26:
            DP[1][sum_num] = 1


    for i in range(2, len(password)):
        if password[i-1]:
            sum_num = password[i-1] * 10 + password[i]

            if 0 < sum_num <= 26:
                DP[i][sum_num] += sum(DP[i-2]) % MOD

        if not password[i]:
            continue
        
        DP[i][password[i]] += sum(DP[i-1]) % MOD

    print(sum(DP[-1]) % MOD)


if __name__ == "__main__":
    solve()