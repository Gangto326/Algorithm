import sys

def solve():
    read = sys.stdin.readline
    N, B, C = map(int, read().split())
    num_list = list(map(int, read().split())) + [0, 0]

    answer = 0
    point = 0
    while point < N:
        if not num_list[point]:
            point += 1
            continue
        
        if B > C:
            answer += num_list[point] * B

            num = min(num_list[point], num_list[point + 1])
            num_list[point] = 0

            answer += num * C
            num_list[point + 1] -= num

            next_num = min(num_list[point + 2] - num_list[point + 1], num)
            
            if next_num < 0:
                next_num = 0

            answer += next_num * C
            num_list[point + 2] -= next_num
        
        else:
            answer += num_list[point] * B

        point += 1
        
    print(answer)


if __name__ == "__main__":
    solve()