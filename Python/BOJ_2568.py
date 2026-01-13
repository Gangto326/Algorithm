import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    MAX_LEN = 500_010

    num_list = [-1] * MAX_LEN

    for _ in range(N):
        start, end = map(int, read().split())
        num_list[end] = start

    min_len_list = []
    index_list = [-1] * MAX_LEN
    for i in range(N):
        if num_list[i] != -1:
            min_len_list.append(num_list[i])
            index_list[i] = len(min_len_list)
            break

    
    def binary_search(index, target):
        nonlocal min_len_list, index_list, num_list

        left = 0
        right = len(min_len_list)

        while left < right:
            mid = (left + right) // 2

            if min_len_list[mid] < target:
                left = mid+1
            
            else:
                right = mid
        
        if left >= len(min_len_list):
            min_len_list.append(target)
            index_list[index] = len(min_len_list)
            return
        
        min_len_list[left] = target
        index_list[index] = left+1

    
    for i in range(MAX_LEN):
        if num_list[i] == -1:
            continue

        binary_search(i, num_list[i])


    max_count = len(min_len_list)
    for i in range(MAX_LEN):
        if index_list[i] == max_count:
            index_list[i] = -1
            max_count -= 1

            for j in range(i-1, -1, -1):
                if max_count == 0:
                    break

                if index_list[j] == max_count:
                    index_list[j] = -1
                    max_count -= 1
            
            break
    
    answer_list = []
    for i in range(MAX_LEN):
        if index_list[i] != -1:
            answer_list.append(num_list[i])
    
    print(len(answer_list))
    answer_list.sort()

    for answer in answer_list:
        print(answer)

if __name__ == "__main__":
    solve()