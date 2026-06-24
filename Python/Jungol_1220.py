import sys

def solve():
    read = sys.stdin.readline
    first = list(read().strip())
    sec = list(read().strip())
    DP = [[0] * (len(first) + 1) for _ in range(len(sec) + 1)]

    for i in range(1, len(sec) + 1):
        sec_word = sec[i - 1]

        for j in range(1, len(first) + 1):
            first_word = first[j - 1]

            if sec_word == first_word:
                DP[i][j] = DP[i-1][j-1] + 1
            
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])

    print(DP[-1][-1])


if __name__ == "__main__":
    solve()