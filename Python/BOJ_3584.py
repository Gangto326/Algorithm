import sys
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.readline
    T = int(read())

    for tc in range(T):
        N = int(read())
        parents = [0] * (N+1)

        for _ in range(N-1):
            A, B = map(int, read().split())
            parents[B] = A
        
        parents_set = set()


        def DFS(index, flag):
            if index == 0:
                return
            
            if flag:
                parents_set.add(index)
                DFS(parents[index], flag)
            
            else:
                if index in parents_set:
                    return index
                
                return DFS(parents[index], flag)


        node, node2 = map(int, read().split())
        DFS(node, True)
        print(DFS(node2, False))


if __name__ == "__main__":
    solve()