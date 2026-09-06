import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))

    dic = dict()
    for i in range(N):
        dic[num_list[i]] = i

    num_list = list(map(int, read().split()))
    index_list = []
    for i in range(N):
        index_list.append(dic[num_list[i]])

    DP = [1] * N
    answer = 1
    for i in range(N):
        for j in range(i + 1, N):
            if index_list[j] > index_list[i]:
                DP[j] = max(DP[j], DP[i] + 1)
                answer = max(answer, DP[j])

    print(answer)
    answer_list = []

    for i in range(DP.index(answer), -1, -1):
        if DP[i] == answer:
            answer_list.append(num_list[i])
            answer -=1

        if answer == 0:
            break

    answer_list.sort()
    print(*answer_list)


if __name__ == "__main__":
    solve()