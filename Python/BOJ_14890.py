import sys

def solve():
    read = sys.stdin.readline
    N, L = map(int, read().split())
    board = [list(map(int, read().split())) for _ in range(N)]

    row_check = [[True] * (N) for _ in range(N)]
    col_check = [[True] * (N) for _ in range(N)]


    def row_search(index):
        nonlocal N

        for i in range(1, N):
            if board[index][i-1] == board[index][i]:
                continue
            
            # 내려가기
            if board[index][i-1] - 1 == board[index][i]:
                for j in range(L):
                    nc = i + j

                    if nc < N and row_check[index][nc] and board[index][i] == board[index][nc]:
                        row_check[index][nc] = False
                    else:
                        return False
            
            # 올라가기
            elif board[index][i-1] + 1 == board[index][i]:
                for j in range(1, L+1):
                    nc = i - j

                    if nc >= 0 and row_check[index][nc] and board[index][i-1] == board[index][nc]:
                        row_check[index][nc] = False
                    else:
                        return False
            
            else:
                return False
        
        return True
    

    def col_search(index):
        nonlocal N

        for i in range(1, N):
            if board[i-1][index] == board[i][index]:
                continue
            
            # 내려가기
            if board[i-1][index] - 1 == board[i][index]:
                for j in range(L):
                    nr = i + j

                    if nr < N and col_check[nr][index] and board[i][index] == board[nr][index]:
                        col_check[nr][index] = False
                    else:
                        return False
            
            # 올라가기
            elif board[i-1][index] + 1 == board[i][index]:
                for j in range(1, L+1):
                    nr = i - j

                    if nr >= 0 and col_check[nr][index] and board[i-1][index] == board[nr][index]:
                        col_check[nr][index] = False
                    else:
                        return False
            
            else:
                return False
        
        return True
    

    answer = 0
    for i in range(N):
        if row_search(i):
            answer += 1
        if col_search(i):
            answer += 1

    print(answer)


if __name__ == "__main__":
    solve()