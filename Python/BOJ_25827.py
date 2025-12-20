import sys

read = sys.stdin.readline

N = int(read())
sum_list = [0] * 100_000

flag = False
for _ in range(N):
    query, start, end = read().split()

    sh, sm, ss = map(int, start.split(":"))
    eh, em, es = map(int, end.split(":"))

    start_time = sh*3600 + sm*60 + ss
    end_time = eh*3600 + em*60 + es

    if query == '1':
        sum_list[start_time] += 1
        sum_list[end_time] -= 1
    
    else:
        if not flag:
            for i in range(1, 100_000):
                sum_list[i] += sum_list[i-1]

            for i in range(1, 100_000):
                sum_list[i] += sum_list[i-1]
            flag = True

        print(sum_list[end_time-1] - sum_list[start_time-1] if start_time != 0 else sum_list[end_time-1])