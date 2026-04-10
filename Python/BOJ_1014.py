import sys

def solve():
    read = sys.stdin.readline
    T = int(read())

    for tc in range(T):
        N, M = map(int, read().split())
        board = [list(read().strip()) for _ in range(N)]

        ALL_VISITED = 1 << M
        case_list = []
        for visited in range(ALL_VISITED):
            if not visited & (visited << 1):
                case_list.append((visited, bin(visited).count('1')))

        DP = [[-1] * ALL_VISITED for _ in range(N)]
        DP[0][0] = 0

        for row in range(N):
            x_binary = 0

            for col in range(M):
                if board[row][col] == 'x':
                    x_binary |= (1 << col)
            
            for visited, count in case_list:
                if visited & x_binary:
                    continue

                if row == 0:
                    DP[0][visited] = count
                    continue
                
                for v, c in case_list:
                    if DP[row - 1][v] == -1:
                        continue

                    if v & (visited << 1) or v & (visited >> 1):
                        continue

                    DP[row][visited] = max(DP[row][visited], DP[row - 1][v] + count)
        
        print(max(DP[-1]))


if __name__ == "__main__":
    solve()