import sys
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    num_list.sort()
    num_dict = defaultdict(int)

    for num in num_list:
        num_dict[num] += 1


    def binary_search(target):
        nonlocal N

        left = 0
        right = N - 1

        while left < right:
            mid = (left + right) // 2

            if num_list[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if num_list[left] == target:
            return left
        
        return -1


    answer = 0
    for i in range(N):
        num = num_list[i]

        for j in range(N):
            if j == i:
                continue
            
            index = binary_search(num - num_list[j])
            if index != -1:
                if num_list[i] == num_list[j] == num_list[index]:
                    if num_dict[num_list[i]] >= 3:
                        answer += 1
                        break
                    
                elif num_list[j] == num_list[index] or num_list[i] == num_list[index]:
                    if num_dict[num_list[index]] >= 2:
                        answer += 1
                        break
                
                else:
                    answer += 1
                    break
    
    print(answer)


if __name__ == "__main__":
    solve()