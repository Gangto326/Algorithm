import sys

read = sys.stdin.readline
N, M = map(int, read().split())

tree_list = [tuple(map(int, read().split())) for _ in range(N)]
people_list = sorted([int(read()) for _ in range(M)])

even_sum = [0, people_list[0]]
odd_sum = [0, 0]
for i in range(1, M):
    if i % 2 == 0:
        even_sum.append(even_sum[-1]+people_list[i])
        odd_sum.append(odd_sum[-1])
    else:
        even_sum.append(even_sum[-1])
        odd_sum.append(odd_sum[-1]+people_list[i])


def binary_search(target):
    left = 0
    right = M

    while left < right:
        mid = (left+right) // 2

        if target > people_list[mid]:
            left = mid + 1
        else:
            right = mid
    
    return left


answer = 0
for start, end in tree_list:
    turn = False if start < end else True
    tree_start = start if not turn else end
    tree_end = end if not turn else start

    start_idx, end_idx = binary_search(tree_start+1), binary_search(tree_end)-1
    if start_idx > end_idx:
        continue
    
    count = end_idx - start_idx + 1
    
    if count % 2 == 0:
        if turn:
            start_idx += 1
        else:
            end_idx -= 1

    even_range = even_sum[end_idx+1] - even_sum[start_idx]
    odd_range = odd_sum[end_idx+1] - odd_sum[start_idx]

    if not turn:
        if start_idx % 2 == 0:
            answer += (even_range - odd_range) - tree_start
        else:
            answer += (odd_range - even_range) - tree_start
        
    else:
        if end_idx % 2 == 0:
            answer += tree_end + (odd_range - even_range)
        else:
            answer += tree_end + (even_range - odd_range)

print(answer)