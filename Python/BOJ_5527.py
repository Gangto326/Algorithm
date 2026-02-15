import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    num_list.append(num_list[-1])

    stack = []
    start = num_list[0]
    count = 1
    for i in range(1, N+1):
        if num_list[i] != start:
            count += 1
            start = num_list[i]
        else:
            stack.append(count)
            count = 1
            start = num_list[i]
    
    
    if len(stack) <= 3:
        print(sum(stack))
    
    else:
        max_num = stack[0] + stack[1] + stack[2]

        answer = max_num
        for i in range(3, len(stack)):
            max_num -= stack[i - 3]
            max_num += stack[i]
            answer = max(answer, max_num)

        print(answer)


if __name__ == "__main__":
    solve()