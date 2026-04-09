import sys
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    N = int(read())
    word = read().strip()

    left = 0
    right = -1
    alpha_dict = defaultdict(int)

    answer = 0
    while right != len(word) - 1:
        right += 1
        alpha_dict[word[right]] += 1

        if len(alpha_dict) > N:
            while len(alpha_dict) > N:
                alpha_dict[word[left]] -= 1

                if alpha_dict[word[left]] == 0:
                    alpha_dict.pop(word[left])

                left += 1

        answer = max(answer, sum(alpha_dict.values()))
                
    print(answer)


if __name__ == "__main__":
    solve()