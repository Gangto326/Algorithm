import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))

    left = 0
    right = N - 1

    answer = [0, 0]
    answer_num = float('inf')

    while left < right:
        sum_num = num_list[left] + num_list[right]

        if abs(sum_num) < answer_num:
            answer_num = abs(sum_num)
            answer = [num_list[left], num_list[right]]

        if sum_num >= 0:
            right -= 1
        else:
            left += 1
    
    print(*answer)


if __name__ == "__main__":
    solve()