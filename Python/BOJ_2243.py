import sys
sys.setrecursionlimit(10 ** 5)

def solve():
    MAX_NUM = 1_000_000
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    tree = [0] * (4 * MAX_NUM)


    def update(index, left, right, target, val):
        if left == right:
            tree[index] += val
            return
        
        mid = (left + right) // 2
        if mid < target:
            update(index * 2 + 1, mid + 1, right, target, val)
        else:
            update(index * 2, left, mid, target, val)

        tree[index] += val
        return


    def exqute_query(index, left, right, target):
        if left == right:
            tree[index] -= 1
            return left
        
        tree[index] -= 1
        mid = (left + right) // 2
        if tree[index * 2] < target:
            return exqute_query(index * 2 + 1, mid + 1, right, target - tree[index * 2])
        else:
            return exqute_query(index * 2, left, mid, target)


    for _ in range(N):
        query = int(next(iterator))

        if query == 2:
            update(1, 0, MAX_NUM, int(next(iterator)), int(next(iterator)))
        else:
            print(exqute_query(1, 0, MAX_NUM, int(next(iterator))))


if __name__ == "__main__":
    solve()