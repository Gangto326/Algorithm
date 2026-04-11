import sys

def solve():
    read = sys.stdin.buffer.readline
    N = int(read())
    num_list = list(map(int, read().split()))

    left = 0
    right = -1
    check = set()
    answer = 0
    while right != (N - 1):
        right += 1

        if not num_list[right] in check:
            check.add(num_list[right])
            answer += len(check)
        
        else:
            flag = False

            while True:
                check.remove(num_list[left])

                if num_list[left] == num_list[right]:
                    flag = True

                left += 1

                if flag:
                    break
            
            check.add(num_list[right])
            answer += len(check)

    print(answer)


if __name__ == "__main__":
    solve()