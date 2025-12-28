import sys

N = int(sys.stdin.read())

answer = []

def DFS(num, stack, result):
    if len(result) == N:
        answer.append(result[:])
        return
    
    if num <= N:
        stack.append(num)
        DFS(num+1, stack, result)
        stack.pop()
    
    if stack:
        result.append(stack.pop())
        DFS(num, stack, result)
        stack.append(result.pop())

DFS(1, [], [])
answer.sort()

for ans in answer:
    print(*ans)