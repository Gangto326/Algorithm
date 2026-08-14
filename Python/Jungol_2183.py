import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(str, read().split()))
    answer = '0'
    check = [True] * N


    def combination(total, count):
        nonlocal N, check, num_list, answer

        if count >= N:
            answer = max(answer, total)
            return

        for i in range(N):
            if check[i]:
                check[i] = False
                combination(total + num_list[i], count + 1)
                check[i] = True
        

    combination('', 0)
    print(answer)


if __name__ == "__main__":
    solve()