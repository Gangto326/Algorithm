import sys

read = sys.stdin.readline
N, K, X = map(int, read().split())
cost_list = list(map(int, read().split()))

before_sum = [0] * (N+1)
after_sum = [0] * (N+1)

for i in range(1, N+1):
    before_sum[i] = before_sum[i-1] + (cost_list[i-1] * X)
    after_sum[N-i] = after_sum[N-i+1] + cost_list[N-i]


def binary_search(left, right, target):
    while left < right:
        mid = (left+right) // 2

        if before_sum[mid] < target:
            left = mid+1
        else:
            right = mid
    
    return left


answer = 0
for i in range(N, -1, -1):
    days = binary_search(0, i, K-after_sum[i])
    if days < 0:
        days = 0
    answer = max(answer, N - ((N-i) + days))

print(answer if answer else -1)