import sys

def solve():
    read = sys.stdin.readline
    N, D = map(int, read().split())
    num_list = list(map(int, read().split()))
    count_list = [0] * (N + 1)

    for num in num_list:
        count_list[num] += 1

    answer = 0
    for count in count_list:
        while count > D:
            answer += 1
            count -= (D - 1)
    
    print(answer)


if __name__ == "__main__":
    solve()