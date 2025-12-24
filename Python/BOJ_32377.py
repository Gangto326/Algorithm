import sys

def solve():
    read = sys.stdin.readline
    N, A, B, C = map(int, read().split())

    ABC_list = [A, B, C]
    char_list = ['A', 'B', 'C']
    left = 0
    right = N * min(ABC_list)

    while left < right:
        mid = (left + right) // 2

        if sum([mid // ABC_list[i] for i in range(3)]) < N:
            left = mid + 1
        else:
            right = mid
    
    count = sum([left // ABC_list[i] for i in range(3)])
    concurrency = sum([left % ABC_list[i] == 0 for i in range(3)])

    count -= concurrency
    for i in range(3):
        if left % ABC_list[i] == 0:
            count += 1

        if count == N:
            print(char_list[i] + " win")
            break


if __name__ == "__main__":
    solve()