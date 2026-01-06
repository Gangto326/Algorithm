import sys

def solve():
    read = sys.stdin.readline
    num_list = list(map(int, read().split()))

    DP = [[1_000_000] * 25 for _ in range(len(num_list))]
    DP[0][0] = 0
    comb_dict = {}
    index_dict = {}

    index = 1
    comb_dict[(0, 0)] = 0
    index_dict[0] = (0, 0)
    for i in range(5):
        for j in range(5):
            if i != j:
                comb_dict[(i, j)] = index
                index_dict[index] = (i, j)
                index += 1

    for i in range(len(num_list)-1):
        for j in range(25):
            if DP[i][j] != 1_000_000:
                left, right = index_dict[j]

                # left 움직이기
                if num_list[i] != right:
                    index = comb_dict[(num_list[i], right)]

                    if left == 0:
                        DP[i+1][index] = min(DP[i+1][index], DP[i][j] + 2)
                    
                    elif left+2 == num_list[i] or left-2 == num_list[i]:
                        DP[i+1][index] = min(DP[i+1][index], DP[i][j] + 4)
                    
                    elif left == num_list[i]:
                        DP[i+1][index] = min(DP[i+1][index], DP[i][j] + 1)

                    elif (4+left-2) % 4 == num_list[i]-1 or (4+left) % 4 == num_list[i]-1:
                        DP[i+1][index] = min(DP[i+1][index], DP[i][j] + 3)
                
                # right 움직이기
                if num_list[i] != left:
                    index = comb_dict[(left, num_list[i])]
                    
                    if right == 0:
                        DP[i+1][index] = min(DP[i+1][index], DP[i][j] + 2)
                    
                    elif right+2 == num_list[i] or right-2 == num_list[i]:
                        DP[i+1][index] = min(DP[i+1][index], DP[i][j] + 4)
                    
                    elif right == num_list[i]:
                        DP[i+1][index] = min(DP[i+1][index], DP[i][j] + 1)

                    elif (4+right-2) % 4 == num_list[i]-1 or (4+right) % 4 == num_list[i]-1:
                        DP[i+1][index] = min(DP[i+1][index], DP[i][j] + 3)

    print(min(DP[-1]))

if __name__ == "__main__":
    solve()