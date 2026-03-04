import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, d, k, c = int(next(iterator)), int(next(iterator)), int(next(iterator)), int(next(iterator))
    sushi_list = [int(next(iterator)) for _ in range(N)]

    for i in range(k + 1):
        sushi_list.append(sushi_list[i])
    
    check = [0] * (d + 1)
    answer = 0
    total = 0
    for i in range(k):
        if not check[sushi_list[i]]:
            total += 1

        check[sushi_list[i]] += 1

    if not check[c]:
        answer = total + 1

    left = 0
    right = k
    while left != N:
        check[sushi_list[left]] -= 1

        if not check[sushi_list[left]]:
            total -= 1

        if not check[sushi_list[right]]:
            total += 1
        
        check[sushi_list[right]] += 1

        if not check[c]:
            answer = max(answer, total + 1)
        else:
            answer = max(answer, total)
        
        left += 1
        right += 1

    print(answer)


if __name__ == "__main__":
    solve()