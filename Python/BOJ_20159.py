import sys

read = sys.stdin.readline
N = int(read())
num_list = list(map(int, read().split()))

half = N//2 + 2
answer = 0
even_sum = [0] * half
odd_sum = [0] * half

for i in range(2, half):
    even_sum[i] = even_sum[i-1] + num_list[(i-2)*2]
    odd_sum[i] = odd_sum[i-1] + num_list[(i-2)*2+1]

for i in range(1, half):
    answer = max(answer, even_sum[i] + odd_sum[half-1]-odd_sum[i], even_sum[i] + odd_sum[half-2]-odd_sum[i-1])

print(answer)