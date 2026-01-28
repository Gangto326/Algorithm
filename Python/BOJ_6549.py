import sys

def solve():
    read = sys.stdin.readline

    while True:
        line = list(map(int, read().split()))

        if line[0] == 0:
            break

        N = line[0]
        num_list = line[1:]
        num_list.append(0)

        stack = []
        answer = 0
        for i, value in enumerate(num_list):

            while stack and num_list[stack[-1]] > value:
                height = num_list[stack.pop()]
                width = i if not stack else (i - stack[-1] - 1)

                answer = max(answer, height * width)
            
            stack.append(i)

        print(answer)


if __name__ == "__main__":
    solve()