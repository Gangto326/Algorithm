import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    S = int(read())

    for i in range(N - 1):
        max_index = i

        for j in range(i + 1, i + S + 1):
            if j >= N:
                break

            if num_list[max_index] < num_list[j]:
                max_index = j
        
        for j in range(max_index, i, -1):
            num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]
            S -= 1
    
    print(*num_list)


if __name__ == "__main__":
    solve()