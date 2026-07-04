import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    a_list, b_list, c_list, d_list = [], [], [], []
    
    idx = 1
    for _ in range(N):
        a_list.append(int(input_data[idx]))
        b_list.append(int(input_data[idx+1]))
        c_list.append(int(input_data[idx+2]))
        d_list.append(int(input_data[idx+3]))
        idx += 4

    ab_dict = {}
    for a in a_list:
        for b in b_list:
            val = a + b
            ab_dict[val] = ab_dict.get(val, 0) + 1

    answer = 0
    for c in c_list:
        for d in d_list:
            target = -(c + d)
            
            if target in ab_dict:
                answer += ab_dict[target]

    print(answer)


if __name__ == "__main__":
    solve()