import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    N = int(next(iterator))
    num_list = [int(next(iterator)) for _ in range(N)]
    answer_list = [0] * N
    
    stack = []
    for i in range(N):
        while stack and num_list[stack[-1]] < num_list[i]:
            num = stack.pop()
            answer_list[num] = i + 1
        
        stack.append(i)

    print("\n".join(list(map(str, answer_list))))
    

if __name__ == "__main__":
    solve()