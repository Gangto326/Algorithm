import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, K = int(next(iterator)), int(next(iterator))
    
    if K >= N:
        print(0)
        return
        
    sensors = [int(next(iterator)) for _ in range(N)]
    sensors.sort()
    
    gaps = []
    for i in range(1, N):
        gaps.append(sensors[i] - sensors[i-1])
        
    gaps.sort(reverse=True)
    answer = sum(gaps[K-1:])
    print(answer)


if __name__ == '__main__':
    solve()