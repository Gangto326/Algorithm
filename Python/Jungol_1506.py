import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    S = int(next(iterator))
    N = int(next(iterator))

    node_list = []
    answer_set = set()

    for _ in range(N):
        n, xn, ymin, ymax = int(next(iterator)), int(next(iterator)), int(next(iterator)), int(next(iterator))
        node_list.append((n, xn, ymin, ymax))
        answer_set.add(n)

    node_list.sort(key = lambda x: x[1])

    y_count = [S] * 1001
    for n, _, ymin, ymax in node_list:
        
        for i in range(ymin, ymax):
            if y_count[i]:
                y_count[i] -= 1

                if n in answer_set:
                    answer_set.remove(n)

    if not answer_set:
        print(0)
    else:
        print(*list(sorted(answer_set)))


if __name__ == "__main__":
    solve()