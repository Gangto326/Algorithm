import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    N, C = int(next(iterator)), int(next(iterator))
    num_list = [int(next(iterator)) for _ in range(N)]
    num_list.sort()


    def binary_search(start, target):
        nonlocal N, num_list

        left = start
        right = N

        while left < right:
            mid = (left + right) // 2

            if num_list[mid] - num_list[start] > target:
                right = mid
            else:
                left = mid + 1
        
        return left


    left = 1
    right = num_list[-1]

    while left < right:
        mid = (left + right) // 2

        index = 0
        count = 0
        while True:
            next_index = binary_search(index, mid)
            
            if next_index != N:
                count += 1
                index = next_index
            else:
                break
        
        if count >= (C - 1):
            left = mid + 1
        else:
            right = mid
    
    print(left)


if __name__ == "__main__":
    solve()