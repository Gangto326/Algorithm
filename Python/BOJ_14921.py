import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))

    left = 0
    right = N-1
    abs_answer = float('inf')
    answer = 0
    while left < right:
        mixed = num_list[left] + num_list[right]

        if abs_answer > abs(mixed):
            abs_answer = abs(mixed)
            answer = mixed

        if not mixed:
            answer = 0
            break

        if mixed < 0:
            left += 1
        else:
            right -= 1

    print(answer)


if __name__ == "__main__":
    solve()