import sys

read = sys.stdin.readline
N, K = map(int, read().split())

sequence = list(map(int, read().split()))
time_list = [[float('inf')] for _ in range(K+1)]
multitab = set()

if N >= K:
    print(0)

else:
    for i in range(K-1, -1, -1):
        time_list[sequence[i]].append(i)

    index = 0
    while len(multitab) < N and index < K:
        app = sequence[index]
        multitab.add(app)
        time_list[app].pop()
        index += 1
    
    answer = 0
    while index < K:
        app = sequence[index]
        time_list[app].pop()
        
        if app in multitab:
            index += 1
        
        else:
            out_index = 0
            max_count = 0
            for run_app in multitab:
                if time_list[run_app][-1] > max_count:
                    max_count = time_list[run_app][-1]
                    out_index = run_app

            multitab.remove(out_index)
            multitab.add(app)
            answer += 1
            index += 1

    print(answer)