import sys
sys.setrecursionlimit(500_000)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    node_list = [[] for _ in range(N + 1)]
    total_comb = (N * (N - 1)) // 2
    answer = 0

    for _ in range(N - 1):
        first, sec = int(next(iterator)), int(next(iterator))

        node_list[first].append(sec)
        node_list[sec].append(first)


    def DFS(index, parents):
        nonlocal N, answer, total_comb

        count = 1

        for node in node_list[index]:
            if node == parents:
                continue

            sub_tree = DFS(node, index)
            up_count = N - sub_tree
            up_comb = (up_count * (up_count - 1)) // 2

            answer += total_comb - up_comb
            count += sub_tree

        return count


    DFS(1, 0)
    print(answer)


if __name__ == "__main__":
    solve()