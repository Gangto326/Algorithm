import sys, heapq

read = sys.stdin.readline
N, M = map(int, read().split())

node_queue = []
for _ in range(M):
    start, end, cost = map(int, read().split())
    heapq.heappush(node_queue, (cost, start, end))

parent = [i for i in range(N+1)]
answer = 0
edge_count = 0


def find(node):
    if parent[node] == node:
        return node
    
    parent[node] = find(parent[node])
    return parent[node]


def union(first, sec):
    first_parent = find(first)
    sec_parent = find(sec)

    if first_parent == sec_parent:
        return False
    
    parent[sec_parent] = first_parent
    return True


while edge_count < N-2:
    cost, start, end = heapq.heappop(node_queue)
    
    if union(start, end):
        answer += cost
        edge_count += 1

print(answer)