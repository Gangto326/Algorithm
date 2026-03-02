import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(lambda x : int(x) % 7, read().split()))

    days = [False] * 7
    days[0] = True

    for num in num_list:
        if not num:
            continue

        can_day = set()
        for i in range(7):
            if days[i]:
                day = (i + num) % 7
                can_day.add(day)
            
        for d in can_day:
            days[d] = True

            if d == 4:
                print("YES")
                return

    print("NO")


if __name__ == "__main__":
    solve()