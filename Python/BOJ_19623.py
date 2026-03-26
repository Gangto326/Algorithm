import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    meeting_list = [(0, 0, 0)]

    for _ in range(N):
        start, end, cost = map(int, read().split())
        meeting_list.append((start, end, cost))
    
    meeting_list.sort(key = lambda x: x[1])
    DP = [0] * (N + 1)


    def binary_search(target, right):
        left = 0

        while left < right:
            mid = (left + right) // 2

            if meeting_list[mid][1] <= target:
                left = mid + 1
            else:
                right = mid

        return left - 1


    for i in range(1, N + 1):
        start, end, cost = meeting_list[i]
        DP[i] = max(DP[i - 1], DP[binary_search(start, i)] + cost)

    print(DP[-1])


if __name__ == "__main__":
    solve()