import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    c_list = list(map(int, read().split()))
    M = int(read())
    boxes = list(map(int, read().split()))

    c_list.sort(reverse = True)
    boxes.sort(reverse = True)

    if boxes[0] > c_list[0]:
        print(-1)
        return

    check = [True] * (M)
    count = 0
    answer = 0
    positions = [0] * N
    while count != M:
        for i in range(N):
            while positions[i] < M:
                if check[positions[i]] and c_list[i] >= boxes[positions[i]]:
                    check[positions[i]] = False
                    count += 1
                    positions[i] += 1
                    break

                positions[i] += 1

        answer += 1

    print(answer)


if __name__ == "__main__":
    solve()