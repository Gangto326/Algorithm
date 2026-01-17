import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = [float('inf')] + list(map(int, read().split()))
    tree = [0] * (4 * N)


    def make_tree(index, left, right, start, end):
        nonlocal tree, num_list

        if right < start or left > end:
            return 0
        
        if left == right:
            tree[index] = left
            return left
        
        mid = (left + right) // 2
        left_min = make_tree(index*2, left, mid, start, end)
        right_min = make_tree(index*2+1, mid+1, right, start, end)

        if num_list[left_min] < num_list[right_min]:
            tree[index] = left_min
        elif num_list[left_min] > num_list[right_min]:
            tree[index] = right_min
        else:
            tree[index] = min(left_min, right_min)
        
        return tree[index]
    

    def update(index, left, right, start, end, target):
        nonlocal num_list, tree

        if left > end or right < start:
            return 0
        
        if left == right:
            return tree[index]
        
        if left <= target and target <= right:
            mid = (left + right) // 2
            left_min = update(index*2, left, mid, start, end, target)
            right_min = update(index*2+1, mid+1, right, start, end, target)

            if num_list[left_min] < num_list[right_min]:
                tree[index] = left_min
            elif num_list[left_min] > num_list[right_min]:
                tree[index] = right_min
            else:
                tree[index] = min(left_min, right_min)
            
        return tree[index]
        
    
    def excute_query(index, left, right, start, end):
        nonlocal tree, num_list

        if left > end or right < start:
            return 0
        
        if left >= start and right <= end:
            return tree[index]
        
        mid = (left + right) // 2
        left_min = excute_query(index*2, left, mid, start, end)
        right_min = excute_query(index*2+1, mid+1, right, start, end)

        if num_list[left_min] < num_list[right_min]:
            return left_min
        elif num_list[left_min] > num_list[right_min]:
            return right_min
        else:
            return min(left_min, right_min)


    make_tree(1, 1, N, 1, N)
    query_num = int(read().rstrip())
    for _ in range(query_num):
        query, i, j = map(int, read().split())

        if query == 1:
            num_list[i] = j
            update(1, 1, N, 1, N, i)
        else:
            print(excute_query(1, 1, N, i, j))


if __name__ == "__main__":
    solve()