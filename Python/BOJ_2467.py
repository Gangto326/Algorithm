import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))

    left = 0
    right = N-1
    total = float('inf')
    answer = [0, 0]

    while left < right:
        sum_num = num_list[left] + num_list[right]
        
        if  abs(sum_num) < total:
            total = abs(sum_num)
            answer = [num_list[left], num_list[right]]
        
        if not total:
            break

        if sum_num < 0:
            left += 1
        else:
            right -= 1
    
    print(*answer)


if __name__ == "__main__":
    solve()