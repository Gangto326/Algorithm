import sys

def solve():
    N, target = map(int, sys.stdin.read().split())
    
    left = 1
    right = 10_000_000_000

    while left < right:
        mid = (left + right) // 2

        total = 0
        for i in range(1, N+1):
            total += min(N, mid // i)
        
        if total < target:
            left = mid + 1
        else:
            right = mid
    
    print(left)


if __name__ == "__main__":
    solve()