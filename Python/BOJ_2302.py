import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    M = int(read())

    comb_list = [1, 1]

    for i in range(40):
        comb_list.append(comb_list[-1] + comb_list[-2])
    
    answer = 1
    location = 1
    for _ in range(M):
        vip = int(read())
        answer *= comb_list[vip - location]
        location = vip + 1
    
    print(answer * comb_list[N - location + 1])


if __name__ == "__main__":
    solve()