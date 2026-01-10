import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))

    answer = 0
    one_score = 0
    two_score = 0
    for i in num_list:
        if i == 1:
            one_score += 1
            two_score -= 1

            if two_score < 0:
                two_score = 0
        else:
            two_score += 1
            one_score -= 1

            if one_score < 0:
                one_score = 0
        
        answer = max(answer, one_score, two_score)
        
    print(answer)


if __name__ == "__main__":
    solve()