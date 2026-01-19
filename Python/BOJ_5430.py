import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    T = int(read().rstrip())

    for tc in range(T):
        p_list = list(read().rstrip())
        N = int(read().rstrip())
        num_list = read().rstrip()
        num_list = deque(num_list[1: -1].split(",")) if N != 0 else deque()

        is_reversed = False
        is_ok = True
        for i in range(len(p_list)):
            if p_list[i] == "R":
                is_reversed = not is_reversed
            
            if p_list[i] == "D":
                if not num_list:
                    print('error')
                    is_ok = False
                    break
                else:
                    if is_reversed:
                        num_list.pop()
                    else:
                        num_list.popleft()
        
        if not is_ok:
            continue

        answer = "["
        if is_reversed:
            while num_list:
                if len(num_list) == 1:
                    answer += str(num_list.pop())
                else:
                    answer += str(num_list.pop()) + ","
        else:
            while num_list:
                if len(num_list) == 1:
                    answer += str(num_list.popleft())
                else:
                    answer += str(num_list.popleft()) + ","
        answer += "]"

        print(answer)


if __name__ == "__main__":
    solve()