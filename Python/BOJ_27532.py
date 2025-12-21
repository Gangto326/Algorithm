import sys

read = sys.stdin.read().split()
iterator = iter(read)
M = int(next(iterator))


def time_calculator(string_time):
    hh, mm = map(int, string_time.split(':'))
    return hh * 60 + mm


time_list = [time_calculator(next(iterator)) for _ in range(M)]

answer = M
for sequence in range(720):
    clock_set = set()

    for i in range(M):
        clock_set.add((time_list[i] - (sequence*i)) % 720)
    
    answer = min(answer, len(clock_set))

print(answer)