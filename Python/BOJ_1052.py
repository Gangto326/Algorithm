import sys

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    bottles = 0
    
    while bin(N).count('1') > K:
        count = N & (-N)
        bottles += count
        N += count
        
    print(bottles)


if __name__ == "__main__":
    solve()