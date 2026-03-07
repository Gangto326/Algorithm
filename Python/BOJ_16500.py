import sys

def solve():
    read = sys.stdin.readline
    S = read().strip()
    S_len = len(S)
    N = int(read())
    word_list = [read().strip() for _ in range(N)]

    DP = [False] * (S_len + 1)
    DP[0] = True

    for i in range(1, S_len + 1):
        for word in word_list:
            w_len = len(word)

            if i >= w_len and DP[i - w_len] and S[i - w_len: i] == word:
                DP[i] = True
                break
    
    print(int(DP[-1]))


if __name__ == "__main__":
    solve()