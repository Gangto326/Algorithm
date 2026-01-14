import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    DP = [[[float('inf'), float('inf'), float('inf')] for _ in range(N)] for _ in range(3)]

    first = list(map(int, read().split()))
    DP[0][0] = [first[0], first[1], float('inf')]
    DP[1][0] = [first[0], float('inf'), first[2]]
    DP[2][0] = [float('inf'), first[1], first[2]]
    
    for i in range(1, N):
        R, G, B = list(map(int, read().split()))

        for j in range(3):
            br, bg, bb = DP[j][i-1]
            DP[j][i] = [R + min(bg, bb), G + min(br, bb), B + min(br, bg)]
    
    
    answer = min(DP[0][-1][2], DP[1][-1][1], DP[2][-1][0])
    print(answer)


if __name__ == "__main__":
    solve()