import sys

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())

    board = [[2] * (N+2)] + [[2] + list(map(int, read().split())) + [2] for _ in range(N)] + [[2] * (N+2)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    horse = {}
    horse_board = [[[] for _ in range(N+2)] for _ in range(N+2)]
    for i in range(1, K+1):
        row, col, move = map(int, read().split())
        horse[i] = [row, col, move-1]
        horse_board[row][col].append(i)

    answer = 0
    flag = False
    while answer <= 1000:
        if flag:
            break

        answer += 1

        for i in range(1, K+1):
            row, col, move = horse[i]
            nr, nc = row + dy[move], col + dx[move]

            index = horse_board[row][col].index(i)
            move_list = horse_board[row][col][index:]

            if board[nr][nc] == 0:
                for move_horse in move_list:
                    horse[move_horse][0], horse[move_horse][1] = nr, nc

                horse_board[nr][nc].extend(move_list)
                horse_board[row][col] = horse_board[row][col][:index]

                if len(horse_board[nr][nc]) >= 4:
                    flag = True
                    break

            elif board[nr][nc] == 1:
                move_list = list(reversed(horse_board[row][col][index:]))

                for move_horse in move_list:
                    horse[move_horse][0], horse[move_horse][1] = nr, nc

                horse_board[nr][nc].extend(move_list)
                horse_board[row][col] = horse_board[row][col][:index]

                if len(horse_board[nr][nc]) >= 4:
                    flag = True
                    break

            else:
                move = move + 1 if move == 0 or move == 2 else move - 1
                nr, nc = row + dy[move], col + dx[move]
                horse[i][2] = move

                if board[nr][nc] == 2:
                    continue

                elif board[nr][nc] == 1:
                    move_list = list(reversed(horse_board[row][col][index:]))
                
                for move_horse in move_list:
                    horse[move_horse][0], horse[move_horse][1] = nr, nc

                horse_board[nr][nc].extend(move_list)
                horse_board[row][col] = horse_board[row][col][:index]
                
                if len(horse_board[nr][nc]) >= 4:
                    flag = True
                    break

    print(answer if flag else -1)


if __name__ == "__main__":
    solve()