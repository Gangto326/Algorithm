import sys, heapq

def solve():
    read = sys.stdin.readline
    N, k = map(int, read().split())
    person_list = [tuple(map(int, read().split())) for _ in range(N)]

    in_queue = []
    out_queue = []

    answer_list = []
    for i in range(min(k, N)):
        heapq.heappush(in_queue, (person_list[i][1], i, person_list[i][0]))
    
    index = min(k, N)
    while index < N:
        min_time = in_queue[0][0]

        while in_queue and in_queue[0][0] == min_time:
            t, num, ids = heapq.heappop(in_queue)
            heapq.heappush(out_queue, (t, -num, ids))

            person = person_list[index]
            heapq.heappush(in_queue, (t+person[1], num, person[0]))
            index += 1

            if index >= N:
                while in_queue and in_queue[0][0] == min_time:
                    t, num, ids = heapq.heappop(in_queue)
                    heapq.heappush(out_queue, (t, -num, ids))
                break
        
        while out_queue:
            t, num, ids = heapq.heappop(out_queue)
            answer_list.append(ids)
    
    while in_queue:
        t, num, ids = heapq.heappop(in_queue)
        heapq.heappush(out_queue, (t, -num, ids))

    while out_queue:
        t, num, ids = heapq.heappop(out_queue)
        answer_list.append(ids)
    
    answer = 0
    for i in range(N):
        answer += answer_list[i] * (i + 1)

    print(answer)


if __name__ == "__main__":
    solve()