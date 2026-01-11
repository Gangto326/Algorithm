import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    K = int(read().rstrip())
    board = [[0] * 7] + [[0] + [1] * 5 + [0] for _ in range(5)] + [[0] * 7]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for _ in range(K):
        row, col = map(int, read().split())
        board[row][col] = 0
    
    finish = 0
    for row in range(7):
        for col in range(7):
            if board[row][col]:
                finish += 1 << (7*row + col)
    
    answer = 0
    BFS = deque()
    BFS.append(((1, 1), (5, 5), (1 << (7*1 + 1)) + (1 << (7*5 + 5))))

    while BFS:
        jungu, heabin, check = BFS.popleft()

        for i in range(4):
            jr, jc = jungu[0] + dx[i], jungu[1] + dy[i]

            if board[jr][jc] and not check & (1 << (7*jr + jc)):
                next_check = check | (1 << (7*jr + jc))

                for j in range(4):
                    hr, hc = heabin[0] + dx[j], heabin[1] + dy[j]

                    if next_check == finish and jr == hr and jc == hc:
                        answer += 1
                        continue

                    if board[hr][hc] and not next_check & (1 << (7*hr + hc)):
                        BFS.append(((jr, jc), (hr, hc), next_check | (1 << (7*hr + hc))))

    print(answer)


if __name__ == "__main__":
    solve()