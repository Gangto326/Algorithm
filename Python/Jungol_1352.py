import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))

    DP = [False] * 15010
    DP[0] = True

    for num in num_list:
        next_num = set()

        for i in range(15000, -1, -1):
            if DP[i]:
                next_num.add(i + num)
                next_num.add(abs(i - num))
        
        for n in next_num:
            DP[n] = True

    M = int(read())
    target_list = list(map(int, read().split()))
    answer_list = []

    for target in target_list:
        if target > 15000:
            answer_list.append("N")

        elif DP[target]:
            answer_list.append("Y")
            
        else:
            answer_list.append("N")
    
    print(*answer_list)


if __name__ == "__main__":
    solve()