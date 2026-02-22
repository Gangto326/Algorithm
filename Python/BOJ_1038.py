import sys

def solve():
    N = int(sys.stdin.readline())
    dec_list = []

    
    def DFS(count, index, nums, limit):

        if count == limit:
            sorted_num = sorted(nums, reverse = True)
            dec_list.append(int(''.join(map(str, sorted_num))))
            return
        
        for i in range(index, 10):
            nums.append(i)
            DFS(count + 1, i + 1, nums, limit)
            nums.pop()
    

    for i in range(1, 11):
        DFS(0, 0, [], i)
    
    dec_list.sort()

    if N >= len(dec_list):
        print(-1)
    else:
        print(dec_list[N])


if __name__ == "__main__":
    solve()