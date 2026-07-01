import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    start, end = map(int, read().split())

    eratos = [True] * 10010
    for i in range(2, 10001):
        if eratos[i]:
            for j in range(i * 2, 10001, i):
                eratos[j] = False
    
    buses = set()
    for i in range(1000, 10001):
        if eratos[i]:
            buses.add(i)
    
    buses.remove(start)
    
    BFS = deque()
    BFS.append((start, 0))


    def can_go(s, e):
        count = 0
        num_list = [1000, 100, 10, 1]

        for i in range(4):
            sn, en = s // num_list[i], e // num_list[i]
            if sn == en:
                count += 1
            
            s -= sn * num_list[i]
            e -= en * num_list[i]
        
        if count == 3:
            return True
        
        return False


    while BFS:
        s, count = BFS.popleft()

        if s == end:
            print(count)
            return
        
        for e in list(buses):
            if can_go(s, e):
                buses.remove(e)
                BFS.append((e, count + 1))


if __name__ == "__main__":
    solve()