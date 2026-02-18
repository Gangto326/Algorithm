import sys
from collections import deque

def solve():
    N = int(sys.stdin.readline())
    DP = [[i, float('inf')] for i in range(N+1)]
    DP[N][1] = 0

    BFS = deque()
    BFS.append((N, 0))

    while BFS:
        num, count = BFS.popleft()

        if num == 1:
            break

        count += 1
        if not num % 3:
            next_num = num // 3

            if DP[next_num][1] > count:
                DP[next_num] = [num, count]
                BFS.append((next_num, count))

        if not num % 2:
            next_num = num // 2

            if DP[next_num][1] > count:
                DP[next_num] = [num, count]
                BFS.append((next_num, count))
        
        next_num = num - 1
        if DP[next_num][1] > count:
            DP[next_num] = [num, count]
            BFS.append((next_num, count))

    answer_list = [1]
    start = 1
    while start != DP[start][0]:
        answer_list.append(DP[start][0])
        start = DP[start][0]

    print(len(answer_list) - 1)
    print(*reversed(answer_list))


if __name__ == "__main__":
    solve()