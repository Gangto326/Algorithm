import sys

def solve():
    read = sys.stdin.readline
    T = int(read().rstrip())

    for tc in range(T):
        N, M = map(int, read().split())

        num_list = list(map(int, read().split()))
        final_list = list(map(int, read().split()))

        flag = True
        for i in range(N-3):
            if num_list[i] != final_list[i]:
                flag = False
                break
        
        if N == M:
            for i in range(N):
                if num_list[i] != final_list[i]:
                    flag = False
                    break

        if not flag:
            print('NO')
            continue

        DP = set()
        DP.add((num_list[-3], num_list[-2], num_list[-1]))

        for i in range(N-3, M-3):
            next_DP = set()

            for x, y, z in DP:
                if x == final_list[i]:
                    for j in range(1, 10, 2):
                        next_DP.add((y, z, j))
                
                if min(x, y, z) == final_list[i]:
                    sort_list = sorted([x, y, z])
                    for j in range(2, 10, 2):
                        next_DP.add((sort_list[-2], sort_list[-1], j))

            if not next_DP:
                DP = next_DP
                break

            DP = next_DP
        
        flag = False
        for x, y, z in DP:
            if x == final_list[-3] and y == final_list[-2] and z == final_list[-1]:
                flag = True
                break
        
        print('YES' if flag else 'NO')


if __name__ == "__main__":
    solve()