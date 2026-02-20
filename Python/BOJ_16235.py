import sys
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    N, M, K = map(int, read().split())
    grow = [list(map(int, read().split())) for _ in range(N)]
    board = [[5] * (N) for _ in range(N)]

    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    tree_dict = defaultdict(list)
    for _ in range(M):
        row, col, age = map(int, read().split())
        row -= 1
        col -= 1
        tree_dict[age].append((row, col))

    dead_list = []


    def spring():
        nonlocal tree_dict

        next_tree_dict = defaultdict(list)

        for i in sorted(tree_dict.keys()):
            for row, col in tree_dict[i]:
                if board[row][col] >= i:
                    board[row][col] -= i
                    next_tree_dict[i+1].append((row, col))
                else:
                    dead_list.append((row, col, i))

        tree_dict = next_tree_dict
    

    def summer():
        nonlocal dead_list

        for row, col, age in dead_list:
            board[row][col] += age // 2
        
        dead_list = []
    

    def autumn():
        nonlocal N
        if not tree_dict:
            return

        for i in range(5, max(tree_dict) + 1, 5):
            if i in tree_dict:
                for row, col in tree_dict[i]:
                    for j in range(8):
                        nr, nc = row + dx[j], col + dy[j]

                        if nr < 0 or nc < 0 or nr >= N or nc >= N:
                            continue

                        tree_dict[1].append((nr, nc))


    def winter():
        for row in range(N):
            for col in range(N):
                board[row][col] += grow[row][col]
    

    for _ in range(K):
        spring()
        summer()
        autumn()
        winter()
    
    answer = 0
    for i in tree_dict.values():
        answer += len(i)
    
    print(answer)


if __name__ == "__main__":
    solve()