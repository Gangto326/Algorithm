import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    N = int(next(iterator))
    num_list = []

    for _ in range(N):
        num_list.append(int(next(iterator)))
    
    stack = []
    answer = 0
    for num in num_list:

        while stack and stack[-1][0] < num:
            answer += stack.pop()[1]
        
        if stack and stack[-1][0] == num:
            count = stack.pop()[1]
            answer += count

            if stack:
                answer += 1
            stack.append((num, count+1))

        else:
            if stack:
                answer += 1
            stack.append((num, 1))

    print(answer)


if __name__ == "__main__":
    solve()