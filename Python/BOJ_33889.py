import sys

def solve():
    MOD = 1_000_000_007
    N, M = map(int, sys.stdin.readline().split())

    DP = [[[(-1, 0)] * 2 for _ in range(M+1)] for _ in range(N+1)]
    DP[0][0][0] = (0, 1)

    for i in range(1, N+1):
        for j in range(M+1):
            # i번째 칸에 사람 비우는 경우
            empty = DP[i-1][j][0]
            not_empty = DP[i-1][j][1]

            score, count = 0, 0
            if empty[0] > not_empty[0]:
                score, count = empty[0], empty[1]
            elif empty[0] < not_empty[0]:
                score, count = not_empty[0], not_empty[1]
            else:
                score, count = empty[0], (empty[1] + not_empty[1]) % MOD
            
            DP[i][j][0] = (score, count)

            # 사람 넣는 경우
            if j > 0:
                empty = DP[i-1][j-1][0]
                empty_score = empty[0] + 2 if empty[0] != -1 else empty[0]

                not_empty = DP[i-1][j-1][1]
                not_empty_score = not_empty[0]

                if empty_score > not_empty_score:
                    DP[i][j][1] = (empty_score, empty[1])
                elif empty_score < not_empty_score:
                    DP[i][j][1] = (not_empty_score, not_empty[1])
                else:
                    DP[i][j][1] = (empty_score, (empty[1]+not_empty[1]) % MOD)

    (es, ec), (nes, nec) = DP[N][M]
    if es > nes:
        print(ec)
    elif es < nes:
        print(nec)
    else:
        print((ec+nec) % MOD)

if __name__ == "__main__":
    solve()