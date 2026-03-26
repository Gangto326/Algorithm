import sys
sys.setrecursionlimit(200_000)

def solve():
    read = sys.stdin.readline

    while True:
        N, M = map(int, read().split())

        if N == M == 0:
            return
        
        edge_list = []
        answer = 0

        for _ in range(M):
            x, y, cost = map(int, read().split())
            answer += cost
            edge_list.append((cost, x, y))
        
        edge_list.sort(key = lambda x: x[0])
        parents = [i for i in range(N + 1)]


        def find(index):
            if parents[index] == index:
                return index
            
            parents[index] = find(parents[index])
            return parents[index]


        def union(a, b):
            ap = find(a)
            bp = find(b)

            if ap == bp:
                return False
            
            parents[ap] = bp
            return True
        

        count = 1
        for cost, x, y in edge_list:
            if union(x, y):
                count += 1
                answer -= cost
            
            if count == N:
                print(answer)
                break


if __name__ == "__main__":
    solve()