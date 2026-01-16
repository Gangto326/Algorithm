import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))

    DP = [[0 if i != j else 1 for i in range(N)] for j in range(N)]
    for i in range(N-1):
        if num_list[i] == num_list[i+1]:
            DP[i][i+1] = 1

    for i in range(2, N):
        for j in range(N-i):
            if num_list[j] == num_list[j+i]:
                if DP[j+1][j+i-1]:
                    DP[j][j+i] = 1
    
    Q = int(read().rstrip())
    for _ in range(Q):
        left, right = map(int, read().split())

        print(DP[left-1][right-1])


if __name__ == "__main__":
    solve()