import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    board = [[1] * (M+2)] + [[1] + list(map(int, list(read().rstrip()))) + [1] for _ in range(N)] + [[1] * (M+2)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    count_list = [0] * 1_000_000
    number = 2
    for row in range(1, N+1):
        for col in range(1, M+1):
            if board[row][col] == 0:
                board[row][col] = number
                count = 1

                BFS = deque()
                BFS.append((row, col))

                while BFS:
                    r, c = BFS.popleft()

                    for way in range(4):
                        nr, nc = r+dx[way], c+dy[way]
                        
                        if board[nr][nc] == 0:
                            BFS.append((nr, nc))
                            count += 1
                            board[nr][nc] = number
                
                count_list[number] = count
                number += 1
    
    for row in range(1, N+1):
        answer = ""

        for col in range(1, M+1):
            if board[row][col] == 1:
                check = set()
                count = 1

                for way in range(4):
                    nr, nc = row + dx[way], col + dy[way]
                    check.add(board[nr][nc])

                for i in check:
                    count += count_list[i]
                
                answer += str(count % 10)
            
            else:
                answer += "0"
        
        print(answer)


if __name__ == "__main__":
    solve()