import sys
sys.setrecursionlimit(200000)

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    in_order = list(map(int, read().split()))
    post_order = list(map(int, read().split()))

    root_dict = {}
    for i in range(N):
        root_dict[in_order[i]] = i


    def DFS(in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return
        
        root = post_order[post_end]
        print(root, end =" ")

        index = root_dict[root]
        left_count = index - in_start

        DFS(in_start, index-1, post_start, post_start + left_count-1)
        DFS(index+1, in_end, post_start + left_count, post_end-1)
    
    DFS(0, N-1, 0, N-1)


if __name__ == "__main__":
    solve()