import sys

def solve():
    read = sys.stdin.readline
    T = int(read().rstrip())

    for tc in range(T):
        K = int(read().rstrip())
        num_list = list(map(int, read().split()))

        sum_nums = [0]
        for num in num_list:
            sum_nums.append(sum_nums[-1] + num)

        DP = [[0] * K for _ in range(K)]

        for step in range(2, K+1):
            for i in range(K - step + 1):
                j = i + step - 1
                DP[i][j] = float('inf')
                total = sum_nums[j+1] - sum_nums[i]

                for k in range(i, j):
                    cost = DP[i][k] + DP[k+1][j] + total
                    if DP[i][j] > cost:
                        DP[i][j] = cost
        
        print(DP[0][-1])
        

if __name__ == "__main__":
    solve()