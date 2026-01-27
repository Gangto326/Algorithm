import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    num_list = list(map(int, read().split()))

    left = max(num_list)
    right = sum(num_list)

    answer = 0
    while left <= right:
        mid = (left + right) // 2

        count = 1
        total = 0
        for num in num_list:
            if total + num <= mid:
                total += num
            else:
                count += 1
                total = num
        
        if count <= M:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == "__main__":
    solve()