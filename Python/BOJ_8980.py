import sys

def solve():
    read = sys.stdin.readline
    N, C = map(int, read().split())
    M = int(read())

    node_list = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, cost = map(int, read().split())
        node_list[start].append((end, cost))
    
    for i in range(N+1):
        node_list[i].sort(key = lambda x: x[0])
    
    car = [0] * (N+1)
    answer = 0
    cost = C

    for i in range(1, N+1):
        answer += car[i]
        cost += car[i]

        car[i] = 0
        for next_node, next_cost in node_list[i]:
            
            if cost < next_cost:
                need = next_cost - cost

                for j in range(N, next_node, -1):
                    if car[j]:
                        if need >= car[j]:
                            need -= car[j]
                            car[j] = 0
                        
                        else:
                            car[j] -= need
                            need = 0
                    
                    if need == 0:
                        break
                
                cost += next_cost - cost - need
            
            car[next_node] += min(cost, next_cost)
            cost -= min(cost, next_cost)

    print(answer)


if __name__ == "__main__":
    solve()