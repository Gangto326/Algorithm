import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))

    left_DP = [1] * N
    right_DP = [1] * N

    for i in range(1, N):
        for j in range(i):
            if num_list[j] < num_list[i]:
                left_DP[i] = max(left_DP[i], left_DP[j]+1)
    
    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if num_list[j] < num_list[i]:
                right_DP[i] = max(right_DP[i], right_DP[j]+1)

    answer = 0
    for i in range(N):
        answer = max(answer, left_DP[i] + right_DP[i] -1)

    print(answer)


if __name__ == "__main__":
    solve()