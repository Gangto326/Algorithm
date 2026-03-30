import sys
sys.setrecursionlimit(200_000)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    parent = [i for i in range(N + 1)]
    
    
    def find(index):
        if parent[index] == index:
            return index
        
        parent[index] = find(parent[index])
        return parent[index]
        

    def union(a, b):
        ap = find(a)
        bp = find(b)
        
        if ap != bp:
            parent[ap] = bp
            return True
        
        return False
        
    
    components = N
    for _ in range(M):
        u, v = int(next(iterator)), int(next(iterator))
        
        if union(u, v):
            components -= 1
            
    answer = M - N + 2 * components - 1
    print(answer)


if __name__ == '__main__':
    solve()