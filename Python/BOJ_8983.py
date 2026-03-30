import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    M, N, L = int(next(iterator)), int(next(iterator)), int(next(iterator))
    hit_point = [int(next(iterator)) for _ in range(M)]
    animals = []

    for _ in range(N):
        x, y = int(next(iterator)), int(next(iterator))
        
        if y <= L:
            animals.append((x, y))

    hit_point.sort(reverse = True)
    animals.sort(key = lambda x: x[0], reverse = True)

    answer = 0
    while hit_point and animals:
        hit = hit_point[-1]

        while animals:
            if abs(animals[-1][0] - hit) + animals[-1][1] <= L:
                answer += 1
                animals.pop()

            else:
                if len(hit_point) != 1 and ((abs(animals[-1][0] - hit) + animals[-1][1]) < (abs(animals[-1][0] - hit_point[-2]) + animals[-1][1])):
                    animals.pop()
                elif animals[-1][0] <= hit:
                    animals.pop()
                else:
                    break
        
        hit_point.pop()
    
    print(answer)


if __name__ == "__main__":
    solve()