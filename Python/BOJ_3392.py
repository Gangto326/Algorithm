import sys
sys.setrecursionlimit(10 ** 5)

def solve():
    MAX_Y = 30_000
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    tree = [0] * (MAX_Y * 4 + 1)
    check = [0] * (MAX_Y * 4 + 1)

    query_list = []
    for _ in range(N):
        x1, y1, x2, y2 = int(next(iterator)), int(next(iterator)), int(next(iterator)), int(next(iterator))
        query_list.append((x1, y1, y2 - 1, 1))
        query_list.append((x2, y1, y2 - 1, -1))

    query_list.sort(key = lambda x: x[0])


    def update(index, start, end, left, right, val):
        if right < start or end < left:
            return
        
        if left <= start and end <= right:
            check[index] += val
        else:
            mid = (start + end) // 2
            update(index * 2, start, mid, left, right, val)
            update(index * 2 + 1, mid + 1, end, left, right, val)
        
        if check[index]:
            tree[index] = end - start + 1
        else:
            if start == end:
                tree[index] = 0
            else:
                tree[index] = tree[index * 2] + tree[index * 2 + 1]
    

    answer = 0
    memo_x = query_list[0][0]

    for x, y1, y2, val in query_list:
        x_len = x - memo_x
        answer += x_len * tree[1]
    
        update(1, 0, MAX_Y - 1, y1, y2, val)

        memo_x = x

    print(answer)


if __name__ == "__main__":
    solve()