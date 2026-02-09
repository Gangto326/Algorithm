import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    point_list = []
    for _ in range(N):
        x, y = int(next(iterator)), int(next(iterator))
        point_list.append((x, y))
    
    point_list.sort(key = lambda x: (x[0], x[1]))


    def ccw(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    

    down_shell = []
    for point in point_list:
        while len(down_shell) >= 2 and ccw(down_shell[-2], down_shell[-1], point) <= 0:
            down_shell.pop()
        
        down_shell.append(point)
    
    up_shell = []
    for point in reversed(point_list):
        while len(up_shell) >= 2 and ccw(up_shell[-2], up_shell[-1], point) <= 0:
            up_shell.pop()
        
        up_shell.append(point)

    answer = 0
    for x, y in down_shell:
        for x1, y1 in up_shell:
            answer = max(answer, (abs(x- x1) ** 2 + abs(y- y1) ** 2) ** 0.5)

    print(answer)


if __name__ == "__main__":
    solve()