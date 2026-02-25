import sys
sys.setrecursionlimit(10**5)

def solve():
    read = sys.stdin.readline
    N, C = map(int, read().split())
    num_list = list(map(int, read().split()))

    half = N // 2
    comb_list = []
    else_comb_list = []

    
    def DFS(index, total):
        nonlocal half
        
        if index >= half:
            comb_list.append(total)
            return

        DFS(index + 1, total)
        DFS(index + 1, total + num_list[index])


    DFS(0, 0)


    def else_DFS(index, total):
        nonlocal N

        if index >= N:
            else_comb_list.append(total)
            return
        
        else_DFS(index + 1, total)
        else_DFS(index + 1, total + num_list[index])
    

    else_DFS(half, 0)
    else_comb_list.sort()


    def binary_search(left, right, target):
        while left < right:
            mid = (left + right) // 2

            if else_comb_list[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        if else_comb_list[left] > target:
            return left - 1
        
        return left
    

    answer = 0
    end = len(else_comb_list) - 1
    for num in comb_list:
        count = binary_search(0, end, C - num) + 1
        answer += count

    print(answer)


if __name__ == "__main__":
    solve()