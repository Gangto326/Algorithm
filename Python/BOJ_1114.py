import sys

def solve():
    read = sys.stdin.readline
    L, K, C = map(int, read().split())
    num_list = [0] + list(map(int, read().split())) + [L]
    num_list.sort()

    left = 0
    right = L
    answer = float('inf')
    while left < right:
        mid = (left + right) // 2

        cut_count = 0
        start = L

        flag = False
        for i in range(K, -1, -1):
            if start - num_list[i] > mid:
                cut_count += 1
                start = num_list[i+1]

                if start - num_list[i] > mid:
                    cut_count = C + 1
                    break
        
        if cut_count <= C and start <= mid:
            flag = True
            
            if cut_count == C:
                answer = start
            else:
                answer = num_list[1]

        if not flag:
            left = mid + 1
        else:
            right = mid
    
    print(left, answer)


if __name__ == "__main__":
    solve()