import sys

def solve():
    read = sys.stdin.readline
    magic = list(read().strip())
    angel = list(read().strip())
    devil = list(read().strip())

    DP_a = [[0] * len(angel) for _ in range(len(magic))]
    DP_d = [[0] * len(devil) for _ in range(len(magic))]

    for i in range(len(angel)):
        if angel[i] == magic[0]:
            DP_a[0][i] = 1
    
    for i in range(len(devil)):
        if devil[i] == magic[0]:
            DP_d[0][i] = 1
    
    for i in range(1, len(magic)):
        for j in range(len(angel)):
            if angel[j] == magic[i]:
                DP_a[i][j] = sum(DP_d[i-1][:j])
        
        for j in range(len(devil)):
            if devil[j] == magic[i]:
                DP_d[i][j] = sum(DP_a[i-1][:j])
    
    print(sum(DP_a[-1]) + sum(DP_d[-1]))


if __name__ == "__main__":
    solve()