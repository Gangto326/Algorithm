import sys
sys.setrecursionlimit(10**6)

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = [0] + list(map(int, read().split()))
    sum_list = [0]

    for i in range(1, N+1):
        sum_list.append(sum_list[-1] + num_list[i])

    tree = [0] * (4*N)


    def make_tree(index, left, right):
        if left == right:
            tree[index] = num_list[left]
            return num_list[left]

        mid = (left + right) // 2
        tree[index] = min(make_tree(index * 2, left, mid), make_tree(index * 2 + 1, mid + 1, right))
        return tree[index]


    answer = -1
    start, end = 0, 0


    def make_query_tree(index, left, right):
        nonlocal answer, start, end

        if left == right:
            total = num_list[left] * num_list[left]

            if answer < total:
                answer = total
                start, end = left, left

            return total

        mid = (left + right) // 2
        result = max(make_query_tree(index * 2, left, mid), make_query_tree(index * 2 + 1, mid + 1, right))
        
        l, r = mid, mid+1
        min_num = min(num_list[l], num_list[r])
        sum_num = num_list[l] + num_list[r]
        total = sum_num * min_num

        if result < total:
            result = total

            if answer < total:
                answer = total
                start, end = l, r

        while l > left or r < right:
            if l > left and r < right:
                if num_list[l-1] >= num_list[r+1]:
                    l -= 1
                    min_num = min(min_num, num_list[l])
                    sum_num += num_list[l]
                else:
                    r += 1
                    min_num = min(min_num, num_list[r])
                    sum_num += num_list[r]
            
            elif l > left:
                l -= 1
                min_num = min(min_num, num_list[l])
                sum_num += num_list[l]
            
            elif r < right:
                r += 1
                min_num = min(min_num, num_list[r])
                sum_num += num_list[r]
            
            total = sum_num * min_num

            if result < total:
                result = total
                
            if answer < total:
                answer = total
                start, end = l, r

        return result
    

    make_tree(1, 1, N)
    make_query_tree(1, 1, N)

    print(answer)
    print(start, end)


if __name__ == "__main__":
    solve()