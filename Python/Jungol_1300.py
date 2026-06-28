import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    num_list = list(map(int, read().split()))

    left = max(num_list)
    right = sum(num_list)

    while left < right:
        mid = (left + right) // 2

        groups = 0
        total = 0
        for i in range(N):
            if total + num_list[i] > mid:
                groups += 1
                total = num_list[i]
            
            else:
                total += num_list[i]
            
            if groups > M:
                break

        if total:
            groups += 1
        
        if groups > M:
            left = mid + 1
        
        else:
            right = mid

    answer_list = []
    total = 0
    count = 0
    for i in range(N):
        if total + num_list[i] > left:
            answer_list.append(count)
            total = num_list[i]
            count = 1
        
        else:
            total += num_list[i]
            count += 1

        if len(answer_list) + (N - i) == M:
            answer_list.append(count)

            for _ in range(i + 1, N):
                answer_list.append(1)

            break
        

    print(left)
    print(*answer_list)


if __name__ == "__main__":
    solve()