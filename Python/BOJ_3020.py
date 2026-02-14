import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, H = int(next(iterator)), int(next(iterator))

    bottom = [0] * (H+1)
    top = [0] * (H+1)

    for i in range(N):
        if i % 2:
            top[int(next(iterator))] += 1
        else:
            bottom[int(next(iterator))] += 1
    
    for i in range(H-1, 0, -1):
        bottom[i] += bottom[i+1]
        top[i] += top[i+1]

    answer = float('inf')
    count = 0
    for i in range(1, H+1):
        break_count = bottom[i] + top[H - i + 1]

        if answer > break_count:
            answer = break_count
            count = 1
        elif answer == break_count:
            count += 1

    print(answer, count)


if __name__ == "__main__":
    solve()