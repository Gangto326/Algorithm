import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    distances = [int(next(iterator)) for _ in range(N)]
    total_length = sum(distances)
    
    left = 0
    right = 0
    curr = 0
    max_answer = 0
    
    for left in range(N):
        while curr < total_length / 2:
            max_answer = max(max_answer, min(curr, total_length - curr))
            curr += distances[right % N]
            right += 1
            
        max_answer = max(max_answer, min(curr, total_length - curr))
        curr -= distances[left]

    print(max_answer)


if __name__ == "__main__":
    solve()