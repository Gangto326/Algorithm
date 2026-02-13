import sys

def solve():
    N = int(sys.stdin.readline())
    answer_list = []

    def DFS(start, end, mid, n):
        if n == 1:
            answer_list.append((start, end))
        
        else:
            DFS(start, mid, end, n-1)
            answer_list.append((start, end))
            DFS(mid, end, start, n-1)
    

    DFS(1, 3, 2, N)
    print(len(answer_list))

    for start, end in answer_list:
        print(start, end)


if __name__ == "__main__":
    solve()