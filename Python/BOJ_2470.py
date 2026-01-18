import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))
    num_list.sort()

    left, right = 0, N-1
    start, end, min_mixed = 0, 0, float('inf')

    while left < right:
        mixed = num_list[left] + num_list[right]

        if abs(mixed) < min_mixed:
            start, end, min_mixed = num_list[left], num_list[right], abs(mixed)
        
        if mixed == 0:
            break
        elif mixed < 0:
            left += 1
        else:
            right -= 1
    
    print(start, end)


if __name__ == "__main__":
    solve()