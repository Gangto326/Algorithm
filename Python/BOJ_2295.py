import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    num_list = [int(next(iterator)) for _ in range(N)]
    num_list.sort()

    two_sum_set = set()
    for i in range(N):
        for j in range(N):
            two_sum_set.add(num_list[i] + num_list[j])

    for i in range(N - 1, -1, -1):
        for j in range(N):
            if num_list[i] - num_list[j] in two_sum_set:
                print(num_list[i])
                return


if __name__ == "__main__":
    solve()