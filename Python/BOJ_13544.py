import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = [0] + list(map(int, read().split()))
    tree = [[] for _ in range(4*N)]


    def make_tree(index, left, right):
        nonlocal tree, num_list
        
        if left == right:
            tree[index].append(num_list[left])
            return tree[index]
        
        mid = (left + right) // 2
        left_list = make_tree(index*2, left, mid)
        right_list = make_tree(index*2+1, mid+1, right)

        l_index = 0
        r_index = 0
        while l_index < len(left_list) and r_index < len(right_list):
            if left_list[l_index] <= right_list[r_index]:
                tree[index].append(left_list[l_index])
                l_index += 1
            else:
                tree[index].append(right_list[r_index])
                r_index += 1
        
        for i in range(l_index, len(left_list)):
            tree[index].append(left_list[i])
        
        for i in range(r_index, len(right_list)):
            tree[index].append(right_list[i])

        return tree[index]


    def excute_query(index, left, right, start, end, target):
        nonlocal tree

        if left > end or right < start:
            return 0
        
        if left >= start and right <= end:

            return len(tree[index]) - binary_search(target, tree[index])
        
        mid = (left + right) // 2
        left_count = excute_query(index*2, left, mid, start, end, target)
        right_count = excute_query(index*2+1, mid+1, right, start, end, target)
        
        return left_count + right_count


    def binary_search(target, merged_list):
        left = 0
        right = len(merged_list)

        while left < right:
            mid = (left + right) // 2

            if merged_list[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return left

    
    make_tree(1, 1, N)
    query_num = int(read().rstrip())
    answer = 0
    for _ in range(query_num):
        a, b, c = map(int, read().split())
        i, j, k = a ^ answer, b ^ answer, c ^ answer
        answer = excute_query(1, 1, N, i, j, k)
        print(answer)
         

if __name__ == "__main__":
    solve()