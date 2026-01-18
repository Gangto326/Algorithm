import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))

    answer_list = [0] * N
    stack = [(float('inf'), 0)]
    for i in range(N-1, -1, -1):
        while stack:
            hight, index = stack[-1]

            if hight <= num_list[i]:
                answer_list[index] = i+1
                stack.pop()
            else:
                break
        
        stack.append((num_list[i], i))
    
    print(*answer_list)



if __name__ == "__main__":
    solve()