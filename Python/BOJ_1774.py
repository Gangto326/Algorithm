import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    space_god = []

    for _ in range(N):
        x, y = map(int, read().split())
        space_god.append((x, y))
    
    edge_list = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = ((space_god[i][0] - space_god[j][0]) ** 2 + (space_god[i][1] - space_god[j][1]) ** 2) ** 0.5
            edge_list.append((cost, i + 1, j + 1))
        
    edge_list.sort(key = lambda x: x[0])
    parents = [i for i in range(N + 1)]


    def find(index):
        if parents[index] == index:
            return parents[index]

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
    answer = 0
    for _ in range(M):
        a, b = map(int, read().split())

        if union(a, b):
            count += 1

    for cost, a, b in edge_list:
        if union(a, b):
            answer += cost
            count += 1
        
        if count == N:
            break
    
    print(f"{answer:.2f}")


if __name__ == "__main__":
    solve()