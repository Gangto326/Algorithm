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


    answer = -2
    stack = []
    for point in point_list:
        while len(stack) >= 2 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        
        stack.append(point)
    
    answer += len(stack)
    stack = []
    for point in reversed(point_list):
        while len(stack) >= 2 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        
        stack.append(point)
    
    print(answer + len(stack))


if __name__ == "__main__":
    solve()