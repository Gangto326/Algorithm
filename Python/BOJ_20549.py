import sys, heapq

read = sys.stdin.readline
N = int(read().rstrip())

night, bishop, rook = map(int, read().split())
night_x = [-2, -1, 1, 2, -2, -1, 1, 2]
night_y = [-1, -2, -2, -1, 1, 2, 2, 1]

bishop_x = [-1, 1, 1, -1]
bishop_y = [-1, -1, 1, 1]

rook_x = [0, 0, 1, -1]
rook_y = [1, -1, 0, 0]

start_s, start_y = map(int, read().split())

M = int(read().rstrip())
food_list = [tuple(map(int, read().split())) for _ in range(M)]
finish = 0
for i in range(M):
    finish += 1 << i

check = [[[float('inf')] * 16 for _ in range(N)] for _ in range(N)]
queue = []

# cost, x, y, 먹이 비트
heapq.heappush(queue, (0, start_s, start_y, 0))
check[start_s][start_y][0] = 0
answer = float('inf')
while queue:
    cost, x, y, bit = heapq.heappop(queue)

    if cost >= answer:
        break

    if bit == finish:
        answer = min(answer, cost)
    
    # 나이트 이동
    for way in range(8):
        n_cost, nx, ny, n_bit = cost + night, x+night_x[way], y+night_y[way], bit

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        for i in range(M):
            if food_list[i][0] == nx and food_list[i][1] == ny:
                n_bit |= 1 << i
                break

        if check[nx][ny][n_bit] > n_cost:
            check[nx][ny][n_bit] = n_cost
            heapq.heappush(queue, (n_cost, nx, ny, n_bit))

    # 비숍 이동
    for way in range(4):
        n_cost, nx, ny = cost + bishop, x+bishop_x[way], y+bishop_y[way]

        while nx >= 0 and ny >= 0 and nx < N and ny < N:
            n_bit = bit

            for i in range(M):
                if food_list[i][0] == nx and food_list[i][1] == ny:
                    n_bit |= 1 << i
                    break

            if check[nx][ny][n_bit] > n_cost:
                check[nx][ny][n_bit] = n_cost
                heapq.heappush(queue, (n_cost, nx, ny, n_bit))
            
            nx += bishop_x[way]
            ny += bishop_y[way]
    
    # 룩 이동
    for way in range(4):
        n_cost, nx, ny = cost + rook, x+rook_x[way], y+rook_y[way]

        while nx >= 0 and ny >= 0 and nx < N and ny < N:
            n_bit = bit

            for i in range(M):
                if food_list[i][0] == nx and food_list[i][1] == ny:
                    n_bit |= 1 << i
                    break

            if check[nx][ny][n_bit] > n_cost:
                check[nx][ny][n_bit] = n_cost
                heapq.heappush(queue, (n_cost, nx, ny, n_bit))
            
            nx += rook_x[way]
            ny += rook_y[way]

print(answer)