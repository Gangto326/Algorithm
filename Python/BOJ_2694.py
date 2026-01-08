import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))

    for tc in range(T):
        N = int(next(iterator))

        num_list = []
        for i in range(N):
            if i == 0:
                num_list.append(int(next(iterator)))
            else:
                num_list.append(int(next(iterator)) + num_list[-1])
        
        
        def binary_search(left, right, target):
            nonlocal num_list, N

            while left < right:
                mid = (left + right) // 2

                if mid >= N:
                    break

                if num_list[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            if left >= N:
                return -1
            
            if num_list[left] == target:
                return left
            
            return -1


        index = 0
        sum_num = 0
        answer = float('inf')
        for i in range(N):
            sum_num = num_list[i]
            index = i

            flag = True
            while index < N-1:
                index = index+1
                index = binary_search(index, N, num_list[index-1] + sum_num)

                if index == -1:
                    flag = False
                    break
            
            if flag:
                answer = sum_num
                break
        
        print(answer)


if __name__ == "__main__":
    solve()