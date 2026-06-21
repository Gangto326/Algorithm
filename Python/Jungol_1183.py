import sys

def solve():
    read = sys.stdin.readline
    W = int(read())
    num_list = list(map(int, read().split()))
    cost_list = [500, 100, 50, 10, 5, 1]

    DP = [-1] * (W + 1)
    DP[0] = 0

    for i in range(5, -1, -1):
        while num_list[i]:
            num_list[i] -= 1
            cost = cost_list[i]

            for j in range(W, -1, -1):
                if j + cost <= W and DP[j] != -1 and DP[j + cost] == -1:
                    DP[j + cost] = j
    
    count_dict = {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 0}
    start_index = W

    while start_index:
        next_index = DP[start_index]
        count_dict[start_index - next_index] += 1
        start_index = next_index
    
    print(sum(count_dict.values()))

    answer = ""
    for cost in cost_list:
        answer += str(count_dict[cost])
        answer += " "
    
    print(answer)


if __name__ == "__main__":
    solve()