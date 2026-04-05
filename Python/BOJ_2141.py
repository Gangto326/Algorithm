import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    x_list = [tuple(map(int, read().split())) for _ in range(N)]
    x_list.sort(key = lambda x: x[0])
    
    total = 0
    for x, a in x_list:
        total += a
    
    target = (total + 1) // 2
    count = 0
    for x, a in x_list:
        count += a

        if count >= target:
            print(x)
            return


if __name__ == "__main__":
    solve()