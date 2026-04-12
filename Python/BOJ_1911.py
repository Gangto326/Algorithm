import sys

def solve():
    read = sys.stdin.buffer.readline
    N, L = map(int, read().split())
    num_list = [list(map(int, read().split())) for _ in range(N)]
    num_list.sort(key = lambda x: x[0])

    start = 0
    answer = 0
    for s, e in num_list:
        if start < s:
            start = s

        count = (e - start) // L + int(bool((e - start) % L))
        answer += count
        start += count * L
    
    print(answer)


if __name__ == "__main__":
    solve()