import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    num_list.sort()

    answer = 0
    for i in range(N - 2):
        left = i + 1
        right = N - 1

        while left < right:
            sum_num = num_list[i] + num_list[left] + num_list[right]

            if sum_num > 0:
                right -= 1
            elif sum_num < 0:
                left += 1
            else:
                if num_list[left] == num_list[right]:
                    count = right - left + 1
                    answer += (count * (count-1)) // 2
                    break
                
                else:
                    left_value = num_list[left]
                    right_value = num_list[right]
                    left_count = 0
                    right_count = 0

                    while left < right and num_list[left] == left_value:
                        left_count += 1
                        left += 1
                    
                    while left <= right and num_list[right] == right_value:
                        right_count += 1
                        right -= 1

                    answer += left_count * right_count

    print(answer)


if __name__ == "__main__":
    solve()