import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    DP = []


    def binary_search(right, target):
        left = 0
        right = right

        while left < right:
            mid = (left + right) // 2

            if DP[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left
    

    for num in num_list:
        if not DP:
            DP.append(num)
        
        index = binary_search(len(DP), num)
        
        if index == len(DP):
            DP.append(num)
        else:
            DP[index] = num

    print(N - len(DP))


if __name__ == "__main__":
    solve()