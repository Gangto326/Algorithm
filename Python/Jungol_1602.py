import sys

def solve():
    read = sys.stdin.readline
    N, L, i = map(int, read().split())


    def count(n, l):
        total = 0
        c = 1
        for k in range(min(n, l) + 1):
            total += c
            c = c * (n - k) // (k + 1)

        return total
    

    result = []
    for pos in range(N):
        remain = N - pos - 1
        cnt = count(remain, L)
        if i <= cnt:
            result.append('0')
        else:
            result.append('1')
            i -= cnt
            L -= 1

    print(''.join(result))


if __name__ == "__main__":
    solve()