import sys

def solve():
    word = sys.stdin.readline().strip()
    sum_list = [1 if word[0] == 'R' else 0]

    for i in range(1, len(word)):
        sum_list.append(sum_list[-1] + int(word[i] == 'R'))
    
    left = -1
    right = len(word)
    answer = sum_list[-1]
    count = 0

    while left < right:
        left += 1
        right -= 1

        while left < right and word[left] != 'K':
            left += 1
        
        while right > left and word[right] != 'K':
            right -= 1
        
        if left >= right:
            break

        count += 1
        r_count = sum_list[right - 1] - sum_list[left]
        
        if r_count > 0:
            answer = max(answer, r_count + count * 2)
    
    print(answer)


if __name__ == "__main__":
    solve()