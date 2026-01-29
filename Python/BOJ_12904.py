import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    S = read().rstrip()
    T = deque(read().rstrip())
    
    is_turn = False

    while len(S) != len(T):
        if is_turn:
            if T[0] == 'B':
                is_turn = not is_turn
            T.popleft()
        else:
            if T[-1] == 'B':
                is_turn = not is_turn
            T.pop()

    answer = ''
    while T:
        if is_turn:
            answer += T.pop()
        else:
            answer += T.popleft()
    
    print(int(S == answer))


if __name__ == "__main__":
    solve()