import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    perm_dict = {}


    def permutation(perm_list, check):
        nonlocal N

        if len(perm_list) == N:
            perm_dict[tuple(perm_list)] = float('inf')
            return

        for i in range(N):
            if check[i]:
                perm_list.append(num_list[i])
                check[i] = False

                permutation(perm_list, check)

                perm_list.pop()
                check[i] = True
    

    check = [True] * N
    permutation([], check)

    M = int(read())
    query_list = []
    for _ in range(M):
        left, right, cost = map(int, read().split())
        query_list.append(tuple([left - 1, right - 1, cost]))

    start = tuple(num_list)
    perm_dict[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    answer_perm = tuple(sorted(num_list))

    while heap:
        cost, perm = heapq.heappop(heap)

        if perm_dict[perm] < cost:
            continue

        if perm_dict[answer_perm] < cost:
            break

        for left, right, c in query_list:
            next_cost = cost + c
            temp = list(perm)

            left_val = temp[left]
            right_val = temp[right]

            temp[left] = right_val
            temp[right] = left_val

            next_perm = tuple(temp)

            if perm_dict[next_perm] > next_cost:
                perm_dict[next_perm] = next_cost
                heapq.heappush(heap, (next_cost, next_perm))

    answer = perm_dict[answer_perm]
    print(answer if answer != float('inf') else -1)


if __name__ == "__main__":
    solve()