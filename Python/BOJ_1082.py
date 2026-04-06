import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    sorted_list = sorted(enumerate(num_list), key = lambda x: (x[1], -x[0]))
    M = int(read())
    curr_M = M

    answer_list = []
    while True:
        if M - sorted_list[0][1] >= 0:
            answer_list.append(sorted_list[0][0])
            M -= sorted_list[0][1]

        else:
            break
    
    for i in range(len(answer_list)):
        num = answer_list[i]

        for j in range(N - 1, num, -1):
            if M >= num_list[j] - num_list[num]:
                answer_list[i] = j
                M -= num_list[j] - num_list[num]
                break
    
    if answer_list[0] == 0:
        answer_list = []
        if N == 1:
            print(0)
            return

        if sorted_list[1][1] <= curr_M:
            answer_list.append(sorted_list[1][0])
            curr_M -= sorted_list[1][1]

            while True:
                if curr_M - sorted_list[0][1] >= 0:
                    answer_list.append(sorted_list[0][0])
                    curr_M -= sorted_list[0][1]

                else:
                    break
            
            for i in range(len(answer_list)):
                num = answer_list[i]

                for j in range(N - 1, num, -1):
                    if curr_M >= num_list[j] - num_list[num]:
                        answer_list[i] = j
                        curr_M -= num_list[j] - num_list[num]
                        break

        else:
            print(0)
            return

    print("".join(map(str, answer_list)))


if __name__ == "__main__":
    solve()