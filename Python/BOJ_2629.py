import sys

def solve():
    MAX_VALUE = 40_010
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))

    DP = [False] * MAX_VALUE
    DP[0] = True

    for i in range(N):
        num = num_list[i]

        for j in range(MAX_VALUE - 1, num - 1, -1):
            if DP[j - num]:
                DP[j] = True

    M = int(read())
    query_list = list(map(int, read().split()))
    total = sum(num_list)
    answer_list = []
    for i in range(M):
        query = query_list[i]

        flag = False
        for j in range(MAX_VALUE - query):
            if DP[j] and DP[j + query] and j + query <= total - j:
                flag = True
                break

        answer_list.append("Y" if flag else "N")

    print(*answer_list)


if __name__ == "__main__":
    solve()