import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    min_list = [0, 0, 0]
    max_list = [0, 0, 0]
    
    for i in range(N):
        query = list(map(int, read().split()))
        min_list = [min(min_list[:2]) + query[0], min(min_list) + query[1], min(min_list[1:]) + query[2]]
        max_list = [max(max_list[:2]) + query[0], max(max_list) + query[1], max(max_list[1:]) + query[2]]
    
    print(max(max_list), min(min_list))


if __name__ == "__main__":
    solve()