import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))

    max_len = []
    index_list = [0] * N


    def binary_search(target):
        left = 0
        right = len(max_len)

        while left < right:
            mid = (left + right) // 2

            if max_len[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left


    for i in range(N):
        num = num_list[i]

        if not max_len:
            max_len.append(num)
            index_list[i] = len(max_len) - 1

        else:
            index = binary_search(num)
            if index == len(max_len):
                max_len.append(num)
                index_list[i] = len(max_len) - 1
            else:
                max_len[index] = num
                index_list[i] = index

    answer = len(max_len)
    answer_list = [0] * answer
    count = answer - 1

    for i in range(N-1, -1, -1):
        if index_list[i] == count:
            answer_list[count] = num_list[i]

            if not count:
                break

            count -= 1
    
    print(answer)
    print(*answer_list)


if __name__ == "__main__":
    solve()