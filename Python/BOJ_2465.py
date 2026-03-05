import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    num_list = []
    for _ in range(N):
        num_list.append(int(next(iterator)))
    num_list.sort()

    tree = [0] * (N * 4)


    def make_tree(index, left, right):
        if left == right:
            tree[index] = 1
            return tree[index]

        mid = (left + right) // 2
        left_val = make_tree(index * 2, left, mid)
        right_val = make_tree(index * 2 + 1, mid + 1, right)

        tree[index] = left_val + right_val
        return tree[index]
    

    def excute_query(index, left, right, target):
        if left == right:
            return left

        mid = (left + right) // 2
        if tree[index * 2] > target:
            return excute_query(index * 2, left, mid, target)
        else:
            return excute_query(index * 2 + 1, mid + 1, right, target - tree[index * 2])


    def update(index, left, right, target):
        if left > target or right < target:
            return
        
        if left == right:
            tree[index] -= 1
            return

        mid = (left + right) // 2
        if mid < target:
            update(index * 2 + 1, mid + 1, right, target)
        else:
            update(index * 2, left, mid, target)
        
        tree[index] -= 1
        return


    make_tree(1, 0, N - 1)
    answer_list = deque()
    query_list = [int(next(iterator)) for _ in range(N)]

    while query_list:
        query = query_list.pop()
        target = excute_query(1, 0, N - 1, query)
        answer_list.appendleft(num_list[target])
        update(1, 0, N - 1, target)
    
    for answer in answer_list:
        print(answer)


if __name__ == "__main__":
    solve()