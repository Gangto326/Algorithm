import sys
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    N = int(read())
    road = read().strip()

    T_sum = [0] * N
    G_sum = [0] * N
    F_sum = [0] * N
    P_sum = [0] * N

    for i in range(N):
        if road[i] == "T":
            T_sum[i] += 1
        elif road[i] == "G":
            G_sum[i] += 1
        elif road[i] == "F":
            F_sum[i] += 1
        else:
            P_sum[i] += 1

    for i in range(1, N):
        T_sum[i] += T_sum[i-1]
        T_sum[i] %= 3
        G_sum[i] += G_sum[i-1]
        G_sum[i] %= 3
        F_sum[i] += F_sum[i-1]
        F_sum[i] %= 3
        P_sum[i] += P_sum[i-1]
        P_sum[i] %= 3

    num_dict = defaultdict(int)
    for i in range(N):
        num_dict[(T_sum[i], G_sum[i], F_sum[i], P_sum[i])] += 1

    answer = num_dict[(0, 0, 0, 0)]
    for i in num_dict:
        answer += num_dict[i] * (num_dict[i] - 1) // 2

    print(answer)


if __name__ == "__main__":
    solve()