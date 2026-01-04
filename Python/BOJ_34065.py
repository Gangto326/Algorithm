import sys
sys.setrecursionlimit(300000)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    
    N = int(next(iterator))
    K = int(next(iterator))
    
    A_list = [int(next(iterator)) for _ in range(N)]
    B_list = [int(next(iterator)) for _ in range(N)]

    A_pos = [0] * (N + 1)
    for i in range(N):
        A_pos[A_list[i]] = i

    B_converted = [A_pos[x] for x in B_list]

    def merge_count(arr):
        if len(arr) <= 1:
            return 0, arr
        
        mid = len(arr) // 2
        cnt_l, left = merge_count(arr[:mid])
        cnt_r, right = merge_count(arr[mid:])
        
        count = cnt_l + cnt_r
        merge = []
        l, r = 0, 0
        n_left, n_right = len(left), len(right)
        
        while l < n_left and r < n_right:
            if left[l] < right[r]:
                count += (n_right - r)
                merge.append(left[l])
                l += 1
            else:
                merge.append(right[r])
                r += 1
        
        merge.extend(left[l:])
        merge.extend(right[r:])
        return count, merge

    total_count, _ = merge_count(B_converted[:])

    if total_count < K:
        print("NO")
        return

    print("YES")

    def merge_sort(arr):
        nonlocal K

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        merge = []
        l, r = 0, 0
        n_left, n_right = len(left), len(right)
        
        while l < n_left and r < n_right:
            if left[l] < right[r]:
                for i in range(r, n_right):
                    sys.stdout.write(f"{A_list[left[l]]} {A_list[right[i]]}\n")
                    
                    K -= 1
                    if K == 0:
                        sys.exit(0)
                
                merge.append(left[l])
                l += 1
            else:
                merge.append(right[r])
                r += 1
        
        merge.extend(left[l:])
        merge.extend(right[r:])
        return merge

    merge_sort(B_converted)

if __name__ == "__main__":
    solve()