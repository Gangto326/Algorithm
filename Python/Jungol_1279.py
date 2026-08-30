import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    M = int(read())
    num_list = list(map(int, read().split()))

    frame = []
    count_list = [0] * 101

    for i in range(M):
        num = num_list[i]

        if num in frame:
            count_list[num] += 1
        
        else:
            if len(frame) == N:
                target = -1
                target_count = float('inf')

                for j in range(N-1, -1, -1):
                    if count_list[frame[j]] <= target_count:
                        target_count = count_list[frame[j]]
                        target = frame[j]
                    
                frame.remove(target)
                count_list[target] = 0

            frame.append(num)
            count_list[num] += 1
        
    print(*frame)


if __name__ == "__main__":
    solve()