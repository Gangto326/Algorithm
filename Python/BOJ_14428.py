import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = [float('inf')] + list(map(int, read().split()))
    tree = [0] * (4 * N)


    def make_tree(index, left, right):
        nonlocal tree, num_list
        
        if left == right:
            tree[index] = left
            return left
        
        mid = (left + right) // 2
        left_min = make_tree(index*2, left, mid)
        right_min = make_tree(index*2+1, mid+1, right)

        if num_list[left_min] < num_list[right_min]:
            tree[index] = left_min
        elif num_list[left_min] > num_list[right_min]:
            tree[index] = right_min
        else:
            tree[index] = min(left_min, right_min)
        
        return tree[index]
    

    def update(index, left, right, target):
        nonlocal num_list, tree
        
        if left == right:
            return tree[index]
        
        mid = (left + right) // 2
        if target <= mid:
            update(index*2, left, mid, target)
        else:
            update(index*2+1, mid+1, right, target)

        if num_list[tree[index*2]] < num_list[tree[index*2+1]]:
            tree[index] = tree[index*2]
        elif num_list[tree[index*2]] > num_list[tree[index*2+1]]:
            tree[index] = tree[index*2+1]
        else:
            tree[index] = min(tree[index*2], tree[index*2+1])
        
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


    make_tree(1, 1, N)
    query_num = int(read().rstrip())
    for _ in range(query_num):
        query, i, j = map(int, read().split())

        if query == 1:
            num_list[i] = j
            update(1, 1, N, i)
        else:
            print(excute_query(1, 1, N, i, j))


if __name__ == "__main__":
    solve()