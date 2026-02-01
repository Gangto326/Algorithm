import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = [0] * (N+1)
    answer_list = []
    check = [True] * (N+1)

    for i in range(1, N+1):
        num = int(read())
        num_list[i] = num

        if num == i:
            answer_list.append(i)
            check[i] = False

    
    def DFS(index, count, start):
        if num_list[index] == start:
            return True
        
        if not cycle_check[num_list[index]]:
            return False
        
        cycle_check[num_list[index]] = False
        return DFS(num_list[index], count + 1, start)


    for i in range(1, N+1):
        cycle_check = check[:]

        if cycle_check[i]:
            if DFS(i, 1, i):
                index = i

                while check[index]:
                    answer_list.append(index)
                    check[index] = False
                    index = num_list[index]
        
    answer_list.sort()
    print(len(answer_list))

    for answer in answer_list:
        print(answer)


if __name__ == "__main__":
    solve()