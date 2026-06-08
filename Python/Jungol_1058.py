import sys

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    num_list = list(map(int, read().split()))

    total = sum(num_list[:K])
    answer = max(0, total)

    left = 0
    right = K

    while right < N:
        total -= num_list[left]
        left += 1

        total += num_list[right]
        right += 1

        answer = max(answer, total)
    
    print(answer)


if __name__ == "__main__":
    solve()