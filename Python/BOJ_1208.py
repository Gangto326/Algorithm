import sys
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    N, S = map(int, read().split())
    num_list = list(map(int, read().split()))

    first_num_list = num_list[:N//2]
    first_dict = defaultdict(int)

    for i in range(len(first_num_list)):
        num = first_num_list[i]
        next_dict = defaultdict(int)
        
        for key in first_dict.keys():
            next_dict[key] += first_dict[key]
            next_dict[key + num] += first_dict[key]

        next_dict[num] += 1
        first_dict = next_dict

    sec_num_list = num_list[N//2:]
    sec_dict = defaultdict(int)
    for i in range(len(sec_num_list)):
        num = sec_num_list[i]
        next_dict = defaultdict(int)
        
        for key in sec_dict.keys():
            next_dict[key] += sec_dict[key]
            next_dict[key + num] += sec_dict[key]

        next_dict[num] += 1
        sec_dict = next_dict
    
    first_nums = sorted(first_dict.keys())
    sec_nums = sorted(sec_dict.keys())


    def binary_search(right, target):
        left = 0
        right = right

        while left < right:
            mid = (left + right) // 2

            if sec_nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if sec_nums[left] == target:
            return True

        return False
    

    r = len(sec_nums) - 1
    answer = sec_dict[S] if binary_search(r, S) else 0
    for num in first_nums:
        if num == S:
            answer += first_dict[num]

        if binary_search(r, S-num):
            answer += first_dict[num] * sec_dict[S-num]

    print(answer)


if __name__ == "__main__":
    solve()