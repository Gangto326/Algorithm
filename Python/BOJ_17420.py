import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    plan_list = list(map(int, read().split()))

    mixed_list = [(num_list[i], plan_list[i]) for i in range(N)]
    mixed_list.sort(key = lambda x: (x[1], x[0]))

    answer = 0
    min_day = 0

    max_day = 0
    before_plan = 0

    for num, plan in mixed_list:
        if before_plan != plan:
            before_plan = plan
            min_day = max(min_day, max_day)

        if num < min_day:
            count = (min_day - num + 29) // 30
            num += count * 30
            answer += count
        
        if num < plan:
            count = (plan - num + 29) // 30
            num += count * 30
            answer += count

        max_day = max(max_day, num)
    
    print(answer)


if __name__ == "__main__":
    solve()