import sys

read = sys.stdin.readline
N = int(read())
num_list = sorted(list(map(int, read().split())))

min_answer = 0
max_answer = 0
index = 0

for i in range(N-1):
    min_answer += num_list[i]
    index += i
    max_answer += num_list[index]

print(min_answer, max_answer)