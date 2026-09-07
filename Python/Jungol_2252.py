import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = sorted(map(int, read().split()))
    print(num_list[(N - 1) // 2], end = " ")

    sum_num = sum(num_list)
    q, r = divmod(sum_num, N)
    print(q + 1 if 2 * r > N else q)


if __name__ == "__main__":
    solve()