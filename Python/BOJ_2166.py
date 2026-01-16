import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())

    points = [tuple(map(int, read().split())) for _ in range(N)]
    points.append(points[0])

    a = 0
    b = 0
    for i in range(N):
        a += points[i][0] * points[i+1][1]
        b += points[i][1] * points[i+1][0]

    print(round(abs(a-b) / 2, 1))


if __name__ == "__main__":
    solve()