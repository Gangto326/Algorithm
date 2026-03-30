import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    arrow_list = [0] * 1_000_010

    answer = 0
    for num in num_list:
        if arrow_list[num]:
            arrow_list[num] -= 1
            arrow_list[num - 1] += 1
        
        else:
            answer += 1
            arrow_list[num - 1] += 1

    print(answer)


if __name__ == "__main__":
    solve()