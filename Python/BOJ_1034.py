import sys
from collections import defaultdict

read = sys.stdin.readline
N, M = map(int, read().split())
lamp_dict = defaultdict(int)

for _ in range(N):
    lamp_dict[read().rstrip()] += 1

lamp_list = sorted(lamp_dict.items(), key = lambda x: x[1], reverse = True)

K = int(read())
answer = 0
for lamp, count in lamp_list:
    zero_count = lamp.count('0')
    
    if zero_count % 2 ==  K % 2 and K >= zero_count:
        answer = count
        break

print(answer)