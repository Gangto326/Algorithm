import sys

read = sys.stdin.readline

N = int(read().rstrip())
num_list = sorted(list(map(int, read().split())))

answer = [float('inf')] * (N*2)
flag = False


def DFS(index, check):
    global flag, answer

    if index >= N*2:
        flag = True
        print(*answer)
        return
    
    if flag:
        return
    
    if answer[index] != float('inf'):
        DFS(index + 1, check)
        return
    
    for i in range(N):
        num = num_list[i]

        if check & (1<<num_list[i]) or index+num+1 >= N*2:
            continue

        if answer[index+num+1] == float('inf'):
            answer[index] = num
            answer[index+num+1] = num

            DFS(index+1, check | (1<<num))

            if flag:
                return

            answer[index] = float('inf')
            answer[index+num+1] = float('inf')


DFS(0, 0)
if not flag:
    print(-1)