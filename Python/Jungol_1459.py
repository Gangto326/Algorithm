import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    num_list = [0] * N
    for i in range(N):
        num_list[i] = int(next(iterator)) - 1
    
    answer_set = set()
    for i in range(N):
        if i in answer_set:
            continue

        start_index = i

        check_list = [True] * N
        check_list[start_index] = False

        num_set = set()
        num_set.add(start_index)

        while True:
            start_index = num_list[start_index]

            if check_list[start_index]:
                check_list[start_index] = False
                num_set.add(start_index)
            else:
                break
        
        if start_index == i:
            answer_set |= num_set

    print(len(answer_set))
    print("\n".join(list(map(lambda x: str(x + 1), sorted(answer_set)))))


if __name__ == "__main__":
    solve()