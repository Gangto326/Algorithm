import sys

def solve():
    MAX_NUM = 100_000_000
    read = sys.stdin.readline
    C, N = map(int, read().split())

    DP = [MAX_NUM] * (C+1)
    DP[0] = 0
    city_list = [tuple(map(int, read().split())) for _ in range(N)]

    for i in range(C):
        if DP[i] != MAX_NUM:

            for j in range(N):
                cost, people = city_list[j]
                next_people = i + people

                if next_people <= C:
                    DP[next_people] = min(DP[next_people], DP[i] + cost)
                
                else:
                    DP[-1] = min(DP[-1], DP[i] + cost)

    print(DP[-1])


if __name__ == "__main__":
    solve()