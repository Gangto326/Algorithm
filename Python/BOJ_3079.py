import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    num_list = []

    max_num = 0
    for _ in range(N):
        num = int(next(iterator))
        num_list.append(num)
        max_num = max(max_num, num)

    left = 0
    right = M * max_num

    while left < right:
        mid = (left + right) // 2

        count = 0
        for num in num_list:
            count += mid // num
        
        if count < M:
            left = mid + 1
        else:
            right = mid
    
    print(left)


if __name__ == "__main__":
    solve()