import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def solve():
    MAX_NUM = 65540
    read = sys.stdin.read().split()
    iterator = iter(read)

    N, K = int(next(iterator)), int(next(iterator))
    tree = [0] * (MAX_NUM * 4)


    def update(index, left, right, target, val):
        if left > target or right < target:
            return

        tree[index] += val

        if left == right:
            return
        
        mid = (left + right) // 2
        update(index * 2, left, mid, target, val)
        update(index * 2 + 1, mid + 1, right, target, val)
    

    def excute_query(index, left, right, target):
        if left == right:
            return left

        mid = (left + right) // 2
        num = 0

        if tree[index * 2] >= target:
            num = excute_query(index * 2, left, mid, target)
        
        else:
            num = excute_query(index * 2 + 1, mid + 1, right, target - tree[index * 2])

        return num

        
    num_list = deque()
    for _ in range(K):
        num = int(next(iterator))
        num_list.append(num)
        update(1, 0, MAX_NUM, num, 1)

    answer = 0
    for _ in range(K, N):
        answer += excute_query(1, 0, MAX_NUM, (K + 1) // 2)

        update(1, 0, MAX_NUM, num_list.popleft(), -1)
        num = int(next(iterator))
        num_list.append(num)
        update(1, 0, MAX_NUM, num, 1)
    answer += excute_query(1, 0, MAX_NUM, (K + 1) // 2)

    print(answer)


if __name__ == "__main__":
    solve()