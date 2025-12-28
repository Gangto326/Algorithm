import sys
sys.setrecursionlimit(200000)
read = sys.stdin.readline
N = int(read())

answer = 0
tree = [[] for _ in range(N+1)]
values = [0] * (N+1)

for i in range(2, N+1):
    animal, cost, parent = read().split()
    cost, parent = int(cost), int(parent)

    if animal == "W":
        cost *= -1
    
    tree[parent].append(i)
    values[i] = cost


def DFS(index):
    value = values[index]

    for child in tree[index]:
        value += DFS(child)
    
    if value < 0:
        return 0
    else:
        return value

print(DFS(1))