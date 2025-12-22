import sys
from bisect import bisect_left

input_data = sys.stdin.read().split()
iterator = iter(input_data)
N = int(next(iterator))

events = []
for _ in range(N):
    s = int(next(iterator))
    e = int(next(iterator))
    c = int(next(iterator))
    events.append((e, s, c))

events.sort()
times = [0]
profits = [0]

for end, start, prize in events:
    idx = bisect_left(times, start)

    if idx == 0:
        prev_profit = 0
    else:
        prev_profit = profits[idx-1]

    current_profit = prev_profit + prize
    
    if current_profit > profits[-1]:
        times.append(end)
        profits.append(current_profit)
        
print(profits[-1])