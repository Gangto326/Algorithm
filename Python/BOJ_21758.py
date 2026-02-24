import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    sum_list = [num_list[0]]
    reversed_sum_list = [sum(num_list)]

    for i in range(1, N):
        sum_list.append(num_list[i] + sum_list[-1])
    
    for i in range(N-1):
        reversed_sum_list.append(reversed_sum_list[-1] - num_list[i])

    answer = 0
    for i in range(N):
        answer = max(answer, sum_list[i] - sum_list[0] + reversed_sum_list[i] - reversed_sum_list[-1])

    for j in range(1, N):
        answer = max(answer, sum_list[-1] * 2 - sum_list[0] - sum_list[j] - num_list[j])

    for j in range(N-2, -1, -1):
        answer = max(answer, reversed_sum_list[0] * 2 - reversed_sum_list[-1] - reversed_sum_list[j] - num_list[j])

    print(answer)


if __name__ == "__main__":
    solve()