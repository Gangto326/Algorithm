import sys
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    students = [[0, 0, 0] for _ in range(N)]
    for i in range(3):
        for j in range(1, N + 1):
            students[int(next(iterator)) - 1][i] = j
    
    students.sort(key = lambda x: x[0])

    tree = [float('inf')] * (N * 4)


    def update(index, start, end, left, right, val):
        if end < left or right < start:
            return tree[index]
        
        if left == right:
            tree[index] = val
            return tree[index]
        
        if start <= left and right <= end:
            tree[index] = min(tree[index], val)
        
        else:
            mid = (left + right) // 2
            left_val = update(index * 2, start, end, left, mid, val)
            right_val = update(index * 2 + 1, start, end, mid + 1, right, val)

            tree[index] = min(left_val, right_val)

        return tree[index]


    def query(index, left, right, start, end):
        if right < start or end < left:
            return float('inf')
        
        if start <= left and right <= end:
            return tree[index]

        mid = (left + right) // 2
        left_val = query(index * 2, left, mid, start, end)
        right_val = query(index * 2 + 1, mid + 1, right, start, end)

        return min(left_val, right_val)


    answer = 0
    for student in students:
        score = query(1, 1, N, 1, student[1] - 1)

        if score > student[2]:
            answer += 1

        update(1, student[1], student[1], 1, N, student[2])

    print(answer)


if __name__ == "__main__":
    solve()