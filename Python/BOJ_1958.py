import sys

def solve():
    read = sys.stdin.readline
    first, sec, third = read().rstrip(), read().rstrip(), read().rstrip()
    f_len, s_len, t_len = len(first), len(sec), len(third)

    DP = [[[0] * (t_len + 1) for _ in range(s_len + 1)] for _ in range(f_len + 1)]

    for i in range(1, f_len + 1):
        for j in range(1, s_len + 1):
            for k in range(1, t_len + 1):
                if first[i-1] == sec[j-1] == third[k-1]:
                    DP[i][j][k] = DP[i-1][j-1][k-1] + 1
                
                else:
                    DP[i][j][k] = max(DP[i-1][j][k], DP[i][j-1][k], DP[i][j][k-1])
    
    print(DP[-1][-1][-1])


if __name__ == "__main__":
    solve()