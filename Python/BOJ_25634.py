import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    on_list = list(map(int, read().split()))
    num = 0

    for i in range(N):
        if on_list[i]:
            num += num_list[i]
            num_list[i] *= - 1

    answer = -float('inf')
    total = 0
    for i in range(N):
        total += num_list[i]
        answer = max(answer, total)

        if total < 0:
            total = 0

    print(num + answer)


if __name__ == "__main__":
    solve()