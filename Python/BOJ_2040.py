import sys
sys.setrecursionlimit(5000)
read = sys.stdin.readline
N = int(read())

for tc in range(3):
    num_list = list(map(int, read().split()))
    num_list.reverse()
    
    DP = [-float('inf')] * N

    def play(idx):
        if idx == N:
            return 0
    
        if DP[idx] != -float('inf'):
            return DP[idx]
        
        sum_num = 0
        max_diff = float('inf')
        for i in range(idx, N):
            sum_num += num_list[i]
            enemy_num = play(i+1)

            if sum_num - enemy_num < max_diff:
                max_diff = sum_num - enemy_num
        
        DP[idx] = max_diff
        return max_diff
    
    play(0)
    
    if DP[0] == 0:
        print("D")
    else:
        print("A" if DP[0] < 0 else "B")