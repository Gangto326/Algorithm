import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    o1,  o2 = map(int, read().split())
    M = int(read())
    target_list = [int(read()) for _ in range(M)]

    DP = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(M)]

    def DFS(index, o1, o2):
        nonlocal M

        if index == M:
            return 0
        
        if DP[index][o1][o2] != -1:
            return DP[index][o1][o2]
        
        target = target_list[index]
        cost1 = abs(target - o1) + DFS(index + 1, target, o2)
        cost2 = abs(target - o2) + DFS(index + 1, o1, target)

        DP[index][o1][o1] = min(cost1, cost2)
        return DP[index][o1][o1]

    print(DFS(0, o1, o2))


if __name__ == "__main__":
    solve()