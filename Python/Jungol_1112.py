import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    min_r, max_r = sorted(map(int, read().split()))
    min_b, max_b = sorted(map(int, read().split()))
    min_y, max_y = sorted(map(int, read().split()))

    start = (max_r + min_r) / 2
    total = max(N - start, start)

    # 정규화
    min_b, max_b = abs(min_b - start), abs(max_b - start)
    min_y, max_y = abs(min_y - start), abs(max_y - start)

    if min_b != max_b:
        start = (min_b + max_b) / 2
        total = max(total - start, start)

        min_y, max_y = abs(min_y - start), abs(max_y - start)
    
    if min_y != max_y:
        start = (min_y + max_y) / 2
        total = max(total - start, start)

    print(f"{total:.1f}")


if __name__ == "__main__":
    solve()