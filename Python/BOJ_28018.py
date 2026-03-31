import sys

def solve():
    MAX_VALUE = 1_000_010
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    sum_list = [0] * MAX_VALUE

    for _ in range(N):
        start, end = int(next(iterator)), int(next(iterator))
        sum_list[start] += 1
        sum_list[end + 1] -= 1
    
    for i in range(1, MAX_VALUE):
        sum_list[i] += sum_list[i - 1]

    Q = int(next(iterator))
    for _ in range(Q):
        print(sum_list[int(next(iterator))])
        

if __name__ == "__main__":
    solve()