import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    M = int(read())
    num_list = list(map(int, read().split()))
    num_list.sort()


    def binary_search(start, target):
        nonlocal N, num_list

        left = start
        right = N - 1

        while left < right:
            mid = (left + right) // 2

            if num_list[mid] < target:
                left = mid + 1
            
            else:
                right = mid
        
        if left >= N:
            return False
        
        if num_list[left] == target:
            return True

        return False
    

    answer = 0
    for i in range(N):
        num = num_list[i]

        if num >= (M / 2):
            break

        else:
            if binary_search(i, M - num):
                answer += 1
    
    print(answer)


if __name__ == "__main__":
    solve()