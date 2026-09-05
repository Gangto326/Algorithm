import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    
    while True:
        N = int(next(iterator))

        if not N:
            break

        floid = [[float('inf')] * (N + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            num = int(next(iterator))
            floid[i][i] = 0

            for _ in range(num):
                node, cost = int(next(iterator)), int(next(iterator))
                floid[i][node] = min(floid[i][node], cost)
        
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                if floid[i][k] == float('inf'):
                    continue

                for j in range(1, N + 1):
                    if i == j:
                        continue

                    floid[i][j] = min(floid[i][j], floid[i][k] + floid[k][j])
        
        answer = 0
        min_num = float('inf')

        for i in range(1, N + 1):
            max_cost = max(floid[i][1:])

            if max_cost < min_num:
                answer = i
                min_num = max_cost
        
        if min_num == float('inf'):
            print("disjoint")

        else:
            print(answer, end = " ")
            print(min_num)


if __name__ == "__main__":
    solve()