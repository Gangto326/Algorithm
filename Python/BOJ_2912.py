import sys

def solve():
    read = sys.stdin.readline
    N, C = map(int, read().split())
    sqrt_num = N ** 0.5
    num_list = [0] + list(map(int, read().split()))

    query_num = int(read().rstrip())
    query_list = []
    for i in range(query_num):
        start, end = map(int, read().split())
        query_list.append((start, end, i))

    query_list.sort(key = lambda x: (x[0] // sqrt_num, x[1] if (x[0] // sqrt_num) % 2 == 0 else -x[1]))
    answer_list = [0] * query_num


    """
    set() 오버헤드로 인해 실패
    """
    # group_set = [set() for _ in range(N+1)]

    # def add(index):
    #     nonlocal max_count

    #     count = hat_list[num_list[index]]
    #     if count > 0:
    #         group_set[count].remove(num_list[index])

    #     count += 1
    #     hat_list[num_list[index]] = count
    #     group_set[count].add(num_list[index])

    #     max_count = max(max_count, count)

    
    # def remove(index):
    #     nonlocal max_count

    #     count = hat_list[num_list[index]]
    #     group_set[count].remove(num_list[index])

    #     if count == max_count and not group_set[count]:
    #         max_count -= 1

    #     count -= 1
    #     hat_list[num_list[index]] = count
    #     group_set[count].add(num_list[index])


    hat_list = [0] * (C + 1)
    head = [0] * (N + 1)

    prev = [0] * (C + 1)
    nxt = [0] * (C + 1)


    def _exclude(c, freq):
        if head[freq] == c:
            head[freq] = nxt[c]
        
        p, n = prev[c], nxt[c]
        if p: nxt[p] = n
        if n: prev[n] = p
        
        prev[c] = 0
        nxt[c] = 0


    def _include(c, freq):
        h = head[freq]
        if h:
            prev[h] = c
            nxt[c] = h
        head[freq] = c


    def add(idx):
        nonlocal max_count
        c = num_list[idx]
        f = hat_list[c]
        
        if f > 0:
            _exclude(c, f)
            
        hat_list[c] += 1
        new_f = f + 1
        
        _include(c, new_f)
        
        if new_f > max_count:
            max_count = new_f


    def remove(idx):
        nonlocal max_count
        c = num_list[idx]
        f = hat_list[c]
        
        _exclude(c, f)
        
        if f == max_count and head[f] == 0:
            max_count -= 1
            
        hat_list[c] -= 1
        new_f = f - 1
        
        if new_f > 0:
            _include(c, new_f)


    left = 1
    right = 0
    max_count = 0
    for i in range(query_num):
        start, end, answer_index = query_list[i]

        while left > start:
            left -= 1
            add(left)

        while right < end:
            right += 1
            add(right)

        while left < start:
            remove(left)
            left += 1
    
        while right > end:
            remove(right)
            right -= 1

        if max_count > ((right - left + 1) / 2):
            answer_list[answer_index] = head[max_count]
            
    for answer in answer_list:
        if not answer:
            print('no')
        else:
            print(f"yes {answer}")
    
if __name__ == "__main__":
    solve()
