import sys
from collections import deque

def solve():
    MOD = 1_000_000_009
    R, C = map(int, sys.stdin.readline().split())

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ux = [[1, -1], [1, -1], [0, 0], [0, 0]]
    uy = [[0, 0], [0, 0], [1, -1], [1, -1]]

    # 좌표: count, 경우의 수
    count_dict = {(1, 1): [0, 1]}
    BFS = deque()

    # row, col, count
    BFS.append((1, 1, 0))
    flag = float('inf')
    while BFS:
        row, col, count = BFS.popleft()
        total = count_dict[(row, col)][1]

        if row == R and col == C:
            flag = count
            continue

        if count >= flag:
            break

        for way in range(4):
            nr, nc = row + dx[way]*2, col + dy[way]*2

            for drift in range(2):
                nnr, nnc = nr + ux[way][drift], nc + uy[way][drift]
                next_count = count + 1

                if nnr <= 0 or nnc <= 0 or nnr > R or nnc > C:
                    continue

                if (nnr, nnc) in count_dict:
                    # BFS라 발생할 일 없을 걸? 아마도
                    if count_dict[(nnr, nnc)][0] > next_count:
                        count_dict[(nnr, nnc)] = [next_count, total]
                        BFS.append((nnr, nnc, next_count))
                    
                    elif count_dict[(nnr, nnc)][0] == next_count:
                        count_dict[(nnr, nnc)][1] += total
                        count_dict[(nnr, nnc)][1] %= MOD
                
                else:
                    count_dict[(nnr, nnc)] = [next_count, total]
                    BFS.append((nnr, nnc, next_count))

    if (R, C) in count_dict:
        print(*count_dict[(R, C)])
    else:
        print("None")


if __name__ == "__main__":
    solve()