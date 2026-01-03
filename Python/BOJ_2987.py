import sys

read = sys.stdin.readline

tri_list = [tuple(map(int, read().split())) for _ in range(3)]

print(int((abs(tri_list[0][0] * (tri_list[1][1] - tri_list[2][1]) + 
          tri_list[1][0] * (tri_list[2][1] - tri_list[0][1]) + 
          tri_list[2][0] * (tri_list[0][1] - tri_list[1][1])) / 2) * 10) / 10)


def cross_product(xa, ya, xb, yb, xp, yp):
    return (xb - xa) * (yp - ya) - (yb - ya) * (xp - xa)


def is_inside(x1, y1, x2, y2, x3, y3, xp, yp):
    cp1 = cross_product(x1, y1, x2, y2, xp, yp)
    cp2 = cross_product(x2, y2, x3, y3, xp, yp)
    cp3 = cross_product(x3, y3, x1, y1, xp, yp)
    
    if (cp1 >= 0 and cp2 >= 0 and cp3 >= 0) or (cp1 <= 0 and cp2 <= 0 and cp3 <= 0):
        return True
    
    return False


N = int(read().rstrip())

answer = 0
for _ in range(N):
    x, y = map(int, read().split())

    if is_inside(*tri_list[0], *tri_list[1], *tri_list[2], x, y):
        answer += 1

print(answer)