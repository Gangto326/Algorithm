import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    sequence = int(read())

    add_list = [0] * (sequence - 1)
    total = sum(num_list[:sequence])
    add_list.append(total)

    for i in range(sequence, N):
        total -= num_list[i - sequence]
        total += num_list[i]
        add_list.append(total)

    DP = [[0] * N for _ in range(3)]
    DP[0][0] = add_list[0]
    for i in range(1, N):
        DP[0][i] = max(DP[0][i - 1], add_list[i])
    
    for i in range(1, 3):
        for j in range(sequence, N):
            DP[i][j] = max(DP[i][j - 1], DP[i - 1][j - sequence] + add_list[j])

    print(DP[2][-1])


if __name__ == "__main__":
    solve()