import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))
    answer = 0


    def merge_sort(num_list):
        nonlocal answer
        
        size = len(num_list)
        if size <= 1:
            return num_list
        
        left_list = merge_sort(num_list[:size // 2])
        right_list = merge_sort(num_list[size // 2:])

        next_list = []
        left = 0
        right = 0
        left_len = len(left_list)
        right_len = len(right_list)

        while left < left_len and right < right_len:
            if left_list[left] <= right_list[right]:
                next_list.append(left_list[left])
                left += 1
            
            else:
                next_list.append(right_list[right])
                right += 1
                answer += (left_len - left)
        
        for i in range(left, left_len):
            next_list.append(left_list[i])
        
        for i in range(right, right_len):
            next_list.append(right_list[i])
        
        return next_list


    merge_sort(num_list)
    print(answer)


if __name__ == "__main__":
    solve()