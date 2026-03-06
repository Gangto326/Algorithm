import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split())) + [0, 0]

    answer = 0
    point = 0
    while point < N:
        if not num_list[point]:
            point += 1
            continue
        
        answer += num_list[point] * 3

        num = min(num_list[point], num_list[point + 1])
        num_list[point] = 0

        answer += num * 2
        num_list[point + 1] -= num

        next_num = min(num_list[point + 2] - num_list[point + 1], num)
        
        if next_num < 0:
            next_num = 0

        answer += next_num * 2
        num_list[point + 2] -= next_num

        point += 1
        
    print(answer)


if __name__ == "__main__":
    solve()