import sys

def solve():
    read = sys.stdin.buffer.readline
    N = int(read())
    spot_list = [tuple(map(int, read().split())) for _ in range(N)]

    MAX_CHECK = 1 << N
    check = [[float('inf')] * MAX_CHECK for _ in range(N)]
    check[0][1] = 0

    for root in range(1, MAX_CHECK):
        if not root & 1:
            continue

        for i in range(N):
            if not root & (1 << i):
                continue

            prev_root = root ^ (1 << i)

            for j in range(N):
                if i == j:
                    continue

                if not prev_root & (1 << j):
                    continue

                if check[j][prev_root] == float('inf'):
                    continue

                check[i][root] = min(check[i][root], check[j][prev_root] + ((spot_list[i][0] - spot_list[j][0]) ** 2 + (spot_list[i][1] - spot_list[j][1]) ** 2) ** 0.5)
    
    answer = float('inf')
    for i in range(1, N):
        answer = min(answer, check[i][MAX_CHECK - 1] + ((spot_list[i][0] - spot_list[0][0]) ** 2 + (spot_list[i][1] - spot_list[0][1]) ** 2) ** 0.5)
    
    print(answer)


if __name__ == "__main__":
    solve()