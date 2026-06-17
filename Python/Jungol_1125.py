import sys
sys.set_int_max_str_digits(100_000)

def solve():
    read = sys.stdin.readline
    keywords = list(read().strip())
    answer = 1
    count = 1

    for keyword in keywords:
        if keyword == 'P':
            continue

        elif keyword == 'L':
            answer *= 2
        
        elif keyword == 'R':
            answer *= 2
            answer += count
        
        else:
            answer *= 5
            answer += count
            count *= 3

    print(answer)


if __name__ == "__main__":
    solve()