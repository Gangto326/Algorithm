import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    num_list.sort()

    tri_list = []
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                mask = (1 << i) | (1 << j) | (1 << k)
                
                if num_list[k] < num_list[i] + num_list[j]:
                    line = (num_list[k] + num_list[i] + num_list[j]) / 2
                    tri_list.append((mask, (line * (line - num_list[k]) * (line - num_list[j]) * (line - num_list[i])) ** 0.5))

    ALL_VISITED = 1 << N
    DP = [0] * ALL_VISITED

    for visited in range(ALL_VISITED):
        for tri_mask, cost in tri_list:
            if not visited & tri_mask:
                next_mask = visited | tri_mask
                DP[next_mask] = max(DP[next_mask], DP[visited] + cost)

    print(DP[-1])


if __name__ == "__main__":
    solve()