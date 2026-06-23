import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    H, F = map(int, read().split())
    points = [tuple(map(int, read().split())) for _ in range(F)]
    points.sort(key = lambda x: x[1])
    point_index = []


    def binary_search(target):
        nonlocal points, F

        left = 0
        right = F

        while left < right:
            mid = (left + right) // 2

            if points[mid][1] < target:
                left = mid + 1
            else:
                right = mid
        
        return left


    BFS = deque()
    check = [True] * F
    for i in range(F):
        x, y = points[i]

        if y <= 1000:
            BFS.append((x, y, 1))
            check[i] = False
        else:
            point_index.append(i)

    goal = H - 1000
    while BFS:
        x, y, count = BFS.popleft()

        if y >= goal:
            print(count)
            return
        
        start_index = binary_search(y - 1000)
        for point in range(start_index, F):
            if check[point]:
                nx, ny = points[point]

                if ny > y + 1000:
                    break

                if (x - nx) ** 2 + (y - ny) ** 2 <= 1000000:
                    check[point] = False
                    BFS.append((nx, ny, count + 1))


if __name__ == "__main__":
    solve()