import sys
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    tree = [0] * (N * 4)

    compressed = [0] * 1_000_010

    def update(index, start, end, target, val):
        if start == end:
            tree[index] += val
            return
        
        mid = (start + end) // 2
        if mid < target:
            update(index * 2 + 1, mid + 1, end, target, val)
        else:
            update(index * 2, start, mid, target, val)
        
        tree[index] += val
        return
    

    for i in range(1, N + 1):
        num = int(next(iterator))
        compressed[num] = i

        update(1, 1, N, i, 1)
    

    def excute_query(index, start, end, target):
        if end <= target:
            return tree[index]
        
        if start > target:
            return 0
        
        mid = (start + end) // 2
        left_val = excute_query(index * 2, start, mid, target)
        right_val = excute_query(index * 2 + 1, mid + 1, end, target)

        return left_val + right_val


    answer = 0
    for _ in range(N):
        num = int(next(iterator))
        target = compressed[num]
        answer += excute_query(1, 1, N, target - 1)

        update(1, 1, N, target, -1)

    print(answer)


if __name__ == "__main__":
    solve()