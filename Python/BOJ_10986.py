import sys
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    num_list = list(map(int, read().split()))
    sum_list = [0]
    num_dict = defaultdict(int)

    for num in num_list:
        sum_list.append((sum_list[-1] + num) % M)
        num_dict[sum_list[-1]] += 1
    
    answer = num_dict[0]
    for num in num_dict.values():
        answer += num * (num-1) // 2
    
    print(answer)


if __name__ == "__main__":
    solve()