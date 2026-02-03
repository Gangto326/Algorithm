import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    class_list = []
    for _ in range(N):
        cost, day = int(next(iterator)), int(next(iterator))
        class_list.append((cost, day))
    
    class_list.sort(key = lambda x: -x[0])
    day_list = [True] * 10_010

    answer = 0
    for i in range(N):
        cost, day = class_list[i]

        for j in range(day, 0, -1):
            if day_list[j]:
                day_list[j] = False
                answer += cost
                break

    print(answer)


if __name__ == "__main__":
    solve()