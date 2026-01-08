import sys

def solve():
    read = sys.stdin.readline
    trash = read()

    N = int(read().rstrip())

    query_list = [None]
    count_list = [0] * (N+1)
    false_counut = 0
    for _ in range(N):
        trash = read()
        students = list(map(int, read().split()))

        if int(read().rstrip()) == 1:
            for i in students:
                count_list[i] += 1
            query_list.append((students, 1))
        else:
            for i in students:
                count_list[i] -= 1
            false_counut += 1
            query_list.append((students, 0))
    
    answer = []
    for i in range(1, N+1):
        if count_list[i] + false_counut == N - 1:
            flag = False

            students, query = query_list[i]
            check = i in students
            if query == 1 and check:
                flag = True
            elif query == 0 and not check:
                flag = True

            if not flag:
                answer.append(i)
    
    if not answer:
        print("swi")
    else:
        print(*answer)


if __name__ == "__main__":
    solve()