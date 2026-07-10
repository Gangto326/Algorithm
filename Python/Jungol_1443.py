import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M, T, K = int(next(iterator)), int(next(iterator)), int(next(iterator)), int(next(iterator))
    node_list = [(int(next(iterator)), int(next(iterator))) for _ in range(T)]

    x_list = [node_list[i][0] for i in range(T)]
    y_list = [node_list[i][1] for i in range(T)]

    answer_node = [0, 0]
    answer = 0
    for x in x_list:
        for y in y_list:
            count = 0

            for node in node_list:
                if (x <= node[0] <= (x + K)) and (y >= node[1] >= (y - K)):
                    count += 1

            if count > answer:
                answer_node = [x, y]
                answer = count
    
    print(*answer_node)
    print(answer)


if __name__ == "__main__":
    solve()