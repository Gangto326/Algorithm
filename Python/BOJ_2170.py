import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    lines = []

    for _ in range(N):
        start, end = map(int, read().split())
        lines.append((start, end))
    
    lines.sort(key = lambda x: x[0])

    answer = lines[0][1] - lines[0][0]
    end = lines[0][1]

    for i in range(1, N):
        s, e = lines[i]

        if s <= end:
            if e > end:
                answer += e - end
                end = e
        
        else:
            end = e
            answer += e - s
    
    print(answer)


if __name__ == "__main__":
    solve()