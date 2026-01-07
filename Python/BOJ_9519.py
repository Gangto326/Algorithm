import sys

def solve():
    read = sys.stdin.readline

    N = int(read().rstrip())
    string_list = list(read().rstrip())
    index_list = [i for i in range(len(string_list))]

    cycle_dict = {}
    history = []

    for i in range(N):
        index_tuple = tuple(index_list)

        if index_tuple in cycle_dict:
            start = cycle_dict[index_tuple]
            cycle_length = i - start
            target = (N-i) % cycle_length
            index_list = history[target]
            break

        else:
            cycle_dict[index_tuple] = i
            history.append(index_tuple)

        left = 0
        right = len(string_list)-1

        index = 0
        next_list = [0] * len(string_list)

        while index < len(string_list):
            next_list[index] = index_list[left]
            left += 1
            index += 1

            if index >= len(string_list):
                break

            next_list[index] = index_list[right]
            right -= 1
            index += 1
        
        index_list = next_list

    answer_list = [0] * len(string_list)
    for i in range(len(string_list)):
        answer_list[index_list[i]] = string_list[i]
    
    print("".join(answer_list))


if __name__ == "__main__":
    solve()