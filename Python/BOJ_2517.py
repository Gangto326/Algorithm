import sys

def solve():
    read = sys.stdin.read().split()
    N = int(read[0])
    query_list = [int(x) for x in read[1:]]

    sorted_index = sorted(range(N), key=lambda i: query_list[i])
    num_list = [0] * N
    for i, index in enumerate(sorted_index, 1):
        num_list[index] = i

    tree = [0] * (N + 1)

    answer = []
    all_count = 0
    for query in range(N):
        num = num_list[query]
        
        index = num
        while index <= N:
            tree[index] += 1
            index += (index & -index)
        
        index = num - 1
        count = 0
        while index > 0:
            count += tree[index]
            index -= (index & -index)

        all_count += 1
        answer.append(str(all_count - count))
    
    sys.stdout.write('\n'.join(answer) + '\n')


if __name__ == '__main__':
    solve()