import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))

    eratos = [True] * 2001
    eratos[0], eratos[1] = False, False
    for i in range(2, 2000):
        if eratos[i]:
            for j in range(i*i, 2000, i):
                eratos[j] = False

    
    def DFS(num, check, selected):
        nonlocal N, group_first, group_sec

        for i in range(N // 2):
            if eratos[num + group_sec[i]] and check[i]:
                check[i] = False

                if selected[i] == -1 or DFS(selected[i], check, selected):
                    selected[i] = num
                    return True
        
        return False


    standard = num_list[0] % 2
    group_first = []
    group_sec = []

    for num in num_list:
        if num % 2 == standard:
            group_first.append(num)
        else:
            group_sec.append(num)

    if len(group_first) != len(group_sec):
        print(-1)
        return
    

    answer_list = []
    for i in range(len(group_sec)):
        if eratos[num_list[0] + group_sec[i]]:
            selected = [-1] * (N // 2)
            selected[i] = group_first[0]

            is_ok = True
            for j in range(1, (N // 2)):
                check = [True] * (N // 2)
                check[i] = False
                
                if not DFS(group_first[j], check, selected):
                    is_ok = False
                    break
            
            if is_ok:
                answer_list.append(group_sec[i])

    answer_list.sort()
    if not answer_list:
        print(-1)
    else:
        print(*answer_list)


if __name__ == "__main__":
    solve()