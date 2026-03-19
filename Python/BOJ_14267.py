import sys
sys.setrecursionlimit(100_010)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    next_node = [[] for _ in range(N + 1)]

    dummy = int(next(iterator))
    for i in range(2, N + 1):
        next_node[int(next(iterator))].append(i)
    
    score_list = [0] * (N + 1)
    for _ in range(M):
        index, score = int(next(iterator)), int(next(iterator))
        score_list[index] += score

    
    def DFS(index, parents):
        score_list[index] += score_list[parents]

        for node in next_node[index]:
            DFS(node, index)
    

    DFS(1, 1)
    print(*score_list[1:])


if __name__ == "__main__":
    solve()