import sys
sys.setrecursionlimit(10_000)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M, K = int(next(iterator)), int(next(iterator)), int(next(iterator))
    num_list = [0] + [int(next(iterator)) for _ in range(N)]
    parents = [i for i in range(N + 1)]
    

    def find(index):
        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index])
        return parents[index]
    

    def union(a, b):
        ap = find(a)
        bp = find(b)

        if ap != bp:
            if num_list[ap] < num_list[bp]:
                num_list[bp] = num_list[ap]

            parents[ap] = bp
            return True

        return False
    

    for _ in range(M):
        a, b = int(next(iterator)), int(next(iterator))
        union(a, b)

    answer = 0
    for i in range(1, N + 1):
        if find(0) != find(i):
            answer += num_list[find(i)]
            union(0, i)
    
    if answer <= K:
        print(answer)
    else:
        print("Oh no")


if __name__ == "__main__":
    solve()