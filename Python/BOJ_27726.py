import sys
from collections import defaultdict
sys.setrecursionlimit(100_010)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    M1, M2, M3 = int(next(iterator)), int(next(iterator)), int(next(iterator))

    parents1 = list(range(N + 1))
    parents2 = list(range(N + 1))
    parents3 = list(range(N + 1))


    def find(index, parents):
        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index], parents)
        return parents[index]
    

    def union(a, b, parents):
        ap = find(a, parents)
        bp = find(b, parents)

        if ap != bp:
            parents[ap] = bp

    
    groups = defaultdict(list)
    for _ in range(M1):
        a, b = int(next(iterator)), int(next(iterator))
        union(a, b, parents1)
    
    for i in range(1, N + 1):
        groups[find(i, parents1)].append(i)
    
    for _ in range(M2):
        a, b = int(next(iterator)), int(next(iterator))
        union(a, b, parents2)
    
    for _ in range(M3):
        a, b = int(next(iterator)), int(next(iterator))
        union(a, b, parents3)

    
    answer_list = []
    for value in groups.values():
        dict = defaultdict(list)

        for num in value:
            dict[(find(num, parents1), find(num, parents2), find(num, parents3))].append(num)
        
        for v in dict.values():
            if len(v) > 1:
                answer_list.append(v)
    
    answer_list.sort(key = lambda x: x[0])
    print(len(answer_list))

    for answer in answer_list:
        print(*answer)
    

if __name__ == '__main__':
    solve()