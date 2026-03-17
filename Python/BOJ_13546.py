import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, K = int(next(iterator)), int(next(iterator))
    num_list = [int(next(iterator)) for _ in range(N)]

    sqrt_num = int(N ** 0.5)
    query_list = []

    M = int(next(iterator))
    for i in range(M):
        l, r = int(next(iterator)) - 1, int(next(iterator)) - 1
        query_list.append((l // sqrt_num, r, l, i))
    
    query_list.sort(key = lambda x: (x[0], x[1]))

    answer_list = [0] * M
    INF = 200_000

    first_idx = [INF] * (K + 1)
    last_idx = [-INF] * (K + 1)

    max_dist = 0
    before_bucket = -1
    pivot = 0
    right = 0

    for bucket, r, l, index in query_list:
        if l // sqrt_num == r // sqrt_num:
            dist = 0
            num_index_dict = {}

            for i in range(l, r + 1):
                num = num_list[i]

                if not num in num_index_dict:
                    num_index_dict[num] = i
                else:
                    dist = max(dist, i - num_index_dict[num])

            answer_list[index] = dist
            continue

        if bucket != before_bucket:
            first_idx = [INF] * (K + 1)
            last_idx = [-INF] * (K + 1)

            max_dist = 0
            before_bucket = bucket
            pivot = (bucket + 1) * sqrt_num
            right = pivot

        while right <= r:
            num = num_list[right]

            if first_idx[num] == INF:
                first_idx[num] = right
            last_idx[num] = right

            max_dist = max(max_dist, last_idx[num] - first_idx[num])
            right += 1

        left = pivot - 1
        temp_dist = max_dist
        num_index_dict = {}

        while left >= l:
            num = num_list[left]
            max_right = 0

            if last_idx[num] != -INF:
                max_right = last_idx[num]

            else:
                if not num in num_index_dict:
                    num_index_dict[num] = left
                else:
                    max_right = num_index_dict[num]

            temp_dist = max(temp_dist, max_right - left)
            left -= 1
        
        answer_list[index] = temp_dist

    answer = ""
    for a in answer_list:
        answer += str(a) + "\n"
    
    print(answer.strip())


if __name__ == "__main__":
    solve()