import sys, heapq

read = sys.stdin.readline
N, K = map(int, read().split())

parents = [i for i in range(N)]
node_list = [[] for _ in range(N)]
min_queue = []


def find(node):
    if parents[node] == node:
        return node
    
    parents[node] = find(parents[node])
    return parents[node]


def union(first, sec):
    first_p = find(first)
    sec_p = find(sec)

    if first_p == sec_p:
        return False

    parents[first_p] = sec_p
    return True


for _ in range(K):
    x, y, cost = map(int, read().split())
    heapq.heappush(min_queue, (cost, x, y))

count = 0
min_answer = 0
while count != N-1:
    cost, x,  y = heapq.heappop(min_queue)
    
    if union(x, y):
        count += 1
        min_answer += cost
        node_list[x].append((y, cost))
        node_list[y].append((x, cost))

print(min_answer)

node_index = 0
max_length = 0
def DFS(index, check, total):
    global node_index, max_length

    if total > max_length:
        max_length = total
        node_index = index

    for next_node, cost in node_list[index]:
        if not next_node in check:
            next_total = total + cost
            check.add(next_node)
            DFS(next_node, check, next_total)
            check.remove(next_node)

check_set = set()
check_set.add(0)
DFS(0, check_set, 0)

check_set = set()
check_set.add(node_index)
DFS(node_index, check_set, 0)

print(max_length)